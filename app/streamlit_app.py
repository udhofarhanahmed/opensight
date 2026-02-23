import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
from datetime import datetime, timedelta

# Page config
st.set_page_config(page_title="OpenSight Dashboard", layout="wide")

# Sidebar
st.sidebar.title("OpenSight")
st.sidebar.image("https://via.placeholder.com/150x50?text=OpenSight", use_container_width=True)
page = st.sidebar.selectbox("Navigate", ["Dashboard", "Data Ingestion", "Insights", "Reports"])

# Backend API URL
API_URL = "http://localhost:8000"

def get_kpis():
    try:
        response = requests.get(f"{API_URL}/api/kpis/summary")
        if response.status_code == 200:
            return response.json()
    except:
        return {"total_revenue": 0.0, "total_orders": 0, "avg_order_value": 0.0}

def get_daily_revenue(days=30):
    try:
        response = requests.get(f"{API_URL}/api/kpis/daily?days={days}")
        if response.status_code == 200:
            return pd.DataFrame(response.json())
    except:
        return pd.DataFrame(columns=['day', 'revenue'])

def get_forecast(days=30):
    try:
        response = requests.get(f"{API_URL}/api/kpis/forecast?days={days}")
        if response.status_code == 200:
            return pd.DataFrame(response.json())
    except:
        return pd.DataFrame(columns=['day', 'revenue'])

def get_insights():
    try:
        response = requests.get(f"{API_URL}/api/insights")
        if response.status_code == 200:
            return response.json()
    except:
        return []

if page == "Dashboard":
    st.title("Sales Intelligence Dashboard")
    
    # Date Range Selector
    st.sidebar.subheader("Filters")
    days_range = st.sidebar.slider("Historical Data Range (Days)", 7, 90, 30)
    
    # Summary Metrics
    kpis = get_kpis()
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"${kpis['total_revenue']:,.2f}")
    col2.metric("Total Orders", f"{kpis['total_orders']:,}")
    col3.metric("Avg Order Value", f"${kpis['avg_order_value']:,.2f}")
    
    # Charts
    st.subheader("Revenue Trends & Forecast")
    df_revenue = get_daily_revenue(days=days_range)
    df_forecast = get_forecast(days=30)
    
    if not df_revenue.empty:
        fig = go.Figure()
        
        # Historical Data
        fig.add_trace(go.Scatter(
            x=df_revenue['day'], 
            y=df_revenue['revenue'],
            name='Historical Revenue',
            line=dict(color='#3498db', width=3)
        ))
        
        # Forecast Data
        if not df_forecast.empty:
            fig.add_trace(go.Scatter(
                x=df_forecast['day'], 
                y=df_forecast['revenue'],
                name='30-Day Forecast',
                line=dict(color='#e67e22', width=2, dash='dash')
            ))
            
        fig.update_layout(
            title=f'Daily Revenue & Forecast',
            xaxis_title='Date',
            yaxis_title='Revenue ($)',
            template='plotly_white',
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No revenue data available yet. Please ingest some data.")

elif page == "Data Ingestion":
    st.title("Data Ingestion")
    st.subheader("Upload CSV or Excel")
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "xls"])
    if uploaded_file is not None:
        if st.button("Upload and Process"):
            try:
                response = requests.post(
                    f"{API_URL}/api/ingest/upload", 
                    files={"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                )
                if response.status_code == 200:
                    st.success(f"Successfully ingested {response.json()['rows']} rows!")
                    # Trigger ETL
                    with st.spinner("Running ETL pipeline..."):
                        requests.post(f"{API_URL}/api/etl/run")
                    st.success("ETL Pipeline completed!")
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Connection error: {e}")

elif page == "Insights":
    st.title("Insight Engine")
    insights = get_insights()
    for insight in insights:
        with st.expander(f"{insight['type'].replace('_', ' ').title()}", expanded=True):
            st.write(insight['description'])
            st.info(f"**Suggested Action:** {insight['suggested_action']}")

elif page == "Reports":
    st.title("PDF Report Generator")
    st.write("Generate a branded PDF leakage report for your business.")
    if st.button("Generate Report"):
        try:
            response = requests.post(f"{API_URL}/api/report/generate")
            if response.status_code == 200:
                st.success("Report generated successfully!")
                st.download_button("Download PDF Report", data=response.content, file_name="opensight_report.pdf", mime="application/pdf")
            else:
                st.error("Failed to generate report.")
        except Exception as e:
            st.error(f"Connection error: {e}")
