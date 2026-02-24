import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
from datetime import datetime, timedelta
import io
from pathlib import Path

# Page config
st.set_page_config(
    page_title="OpenSight Pro | Sales Intelligence",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    css_file = Path(__file__).parent / "style.css"
    if css_file.exists():
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        # Fallback inline CSS if file not found
        st.markdown("""
        <style>
        .main-header { background: #1e293b; color: white; padding: 2rem; border-radius: 12px; margin-bottom: 2rem; }
        .metric-card { background: white; padding: 1.5rem; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .metric-card h3 { color: #64748b; font-size: 0.875rem; margin-bottom: 0.5rem; }
        .metric-card .value { font-size: 1.875rem; font-weight: 700; color: #0f172a; }
        .delta-up { color: #10b981; font-size: 0.875rem; }
        .delta-down { color: #ef4444; font-size: 0.875rem; }
        </style>
        """, unsafe_allow_html=True)

load_css()

# API URL
API_URL = "http://localhost:8000"

# Helper functions
def fetch_kpis(days=30):
    try:
        response = requests.get(f"{API_URL}/api/kpis/summary?days={days}")
        return response.json() if response.status_code == 200 else None
    except: return None

def fetch_daily_revenue(days=30):
    try:
        response = requests.get(f"{API_URL}/api/kpis/daily?days={days}")
        return pd.DataFrame(response.json()) if response.status_code == 200 else pd.DataFrame()
    except: return pd.DataFrame()

def fetch_forecast(days=30):
    try:
        response = requests.get(f"{API_URL}/api/kpis/forecast?days={days}")
        return pd.DataFrame(response.json()) if response.status_code == 200 else pd.DataFrame()
    except: return pd.DataFrame()

def fetch_insights():
    try:
        response = requests.get(f"{API_URL}/api/insights")
        return response.json() if response.status_code == 200 else []
    except: return []

# Sidebar
with st.sidebar:
    st.markdown("# 📈 OpenSight Pro")
    st.markdown("---")
    page = st.radio("Navigation", ["Dashboard", "Data Ingestion", "Insights", "Reports"])
    
    st.markdown("---")
    st.subheader("Quick Actions")
    if st.button("🚀 Load Sample Data", use_container_width=True, help="Instantly populate the dashboard with demo data"):
        with st.spinner("Generating demo data..."):
            try:
                res = requests.post(f"{API_URL}/api/sample-data")
                if res.status_code == 200:
                    st.success("Sample data loaded!")
                    st.rerun()
            except:
                st.error("Could not connect to API")

# Dashboard Page
if page == "Dashboard":
    st.markdown('<div class="main-header"><h1>Sales Intelligence Dashboard</h1><p>Real-time performance tracking and revenue forecasting</p></div>', unsafe_allow_html=True)
    
    # Filters
    col_f1, col_f2 = st.columns([1, 3])
    with col_f1:
        days_range = st.selectbox("Analysis Period", [7, 14, 30, 60, 90], index=2, format_func=lambda x: f"Last {x} Days")
    
    # Metrics
    kpis = fetch_kpis(days=days_range)
    if kpis:
        c1, c2, c3 = st.columns(3)
        
        def render_metric(col, label, value, delta, prefix="$"):
            with col:
                delta_class = "delta-up" if delta >= 0 else "delta-down"
                delta_icon = "↑" if delta >= 0 else "↓"
                st.markdown(f"""
                <div class="metric-card">
                    <h3>{label}</h3>
                    <div class="value">{prefix}{value:,.2f}</div>
                    <div class="delta {delta_class}">{delta_icon} {abs(delta):.1f}% vs prev. period</div>
                </div>
                """, unsafe_allow_html=True)

        render_metric(c1, "Total Revenue", kpis['total_revenue'], kpis['revenue_change'])
        render_metric(c2, "Total Orders", kpis['total_orders'], kpis['orders_change'], prefix="")
        render_metric(c3, "Avg Order Value", kpis['avg_order_value'], kpis['aov_change'])
    
    # Charts
    st.markdown("---")
    col_c1, col_c2 = st.columns([2, 1])
    
    with col_c1:
        st.subheader("Revenue Trends & Forecast")
        df_rev = fetch_daily_revenue(days=days_range)
        df_fore = fetch_forecast(days=30)
        
        if not df_rev.empty:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df_rev['day'], y=df_rev['revenue'], name='Historical', line=dict(color='#3b82f6', width=3)))
            if not df_fore.empty:
                fig.add_trace(go.Scatter(x=df_fore['day'], y=df_fore['revenue'], name='Forecast', line=dict(color='#f59e0b', width=2, dash='dash')))
            
            fig.update_layout(margin=dict(l=0, r=0, t=30, b=0), height=400, template="plotly_white", hovermode="x unified")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data available. Use 'Load Sample Data' in the sidebar to see a demo.")

    with col_c2:
        st.subheader("Channel Performance")
        # Mock data for channel if not in API yet
        channel_data = pd.DataFrame({
            "Channel": ["Instagram", "WhatsApp", "Web", "Facebook"],
            "Revenue": [4500, 3200, 2100, 1200]
        })
        fig_pie = px.pie(channel_data, values='Revenue', names='Channel', hole=.4, color_discrete_sequence=px.colors.qualitative.Pastel)
        fig_pie.update_layout(margin=dict(l=0, r=0, t=30, b=0), height=400)
        st.plotly_chart(fig_pie, use_container_width=True)

    # Export Section
    st.markdown("---")
    st.subheader("📤 Export Data")
    exp_col1, exp_col2, exp_col3 = st.columns(3)
    
    with exp_col1:
        if not df_rev.empty:
            csv = df_rev.to_csv(index=False)
            st.download_button("Download CSV", csv, "revenue_data.csv", "text/csv", use_container_width=True)
    
    with exp_col2:
        if not df_rev.empty:
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                df_rev.to_excel(writer, index=False)
            st.download_button("Download Excel", buffer.getvalue(), "revenue_data.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", use_container_width=True)
            
    with exp_col3:
        st.info("💡 Tip: Use the 'Reports' page for a full PDF summary.")

# Data Ingestion Page
elif page == "Data Ingestion":
    st.title("📥 Data Ingestion")
    st.markdown("Upload your sales data to update the dashboard.")
    
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx", "xls"])
    
    if uploaded_file:
        df_preview = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        st.subheader("Data Preview")
        st.dataframe(df_preview.head(5), use_container_width=True)
        
        st.subheader("Column Mapping")
        st.info("Map your file columns to OpenSight fields")
        
        cols = st.columns(3)
        mapping = {}
        fields = ["order_id", "amount", "customer_id", "timestamp", "channel"]
        
        for i, field in enumerate(fields):
            with cols[i % 3]:
                mapping[field] = st.selectbox(f"Field: {field}", options=df_preview.columns, index=i if i < len(df_preview.columns) else 0)
        
        if st.button("Process & Ingest Data", type="primary"):
            with st.spinner("Ingesting data..."):
                import json
                try:
                    # Reset file pointer
                    uploaded_file.seek(0)
                    response = requests.post(
                        f"{API_URL}/api/ingest/upload", 
                        files={"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)},
                        data={"mapping": json.dumps(mapping)}
                    )
                    if response.status_code == 200:
                        requests.post(f"{API_URL}/api/etl/run")
                        st.success("Data successfully ingested and processed!")
                        st.balloons()
                    else:
                        st.error(f"Upload failed: {response.text}")
                except Exception as e:
                    st.error(f"API Connection Error: {e}")

# Insights Page
elif page == "Insights":
    st.title("💡 Smart Insights")
    insights = fetch_insights()
    
    if insights:
        for ins in insights:
            with st.container():
                st.markdown(f"""
                <div style="background: white; padding: 1.5rem; border-radius: 12px; border-left: 5px solid #3b82f6; margin-bottom: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                    <h4 style="margin:0; color:#1e293b;">{ins['type'].replace('_', ' ').title()}</h4>
                    <p style="color:#64748b; margin: 0.5rem 0;">{ins['description']}</p>
                    <div style="background:#eff6ff; padding:0.5rem 1rem; border-radius:6px; color:#1d4ed8; font-size:0.875rem;">
                        <strong>Action:</strong> {ins['suggested_action']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("No insights generated yet. Ingest data to see recommendations.")

# Reports Page
elif page == "Reports":
    st.title("📄 Executive Reports")
    st.markdown("Generate and download professional PDF reports.")
    
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        st.markdown("""
        ### Branded Leakage Report
        Includes:
        - Executive Summary
        - KPI Performance
        - Revenue Forecast
        - Actionable Insights
        """)
        if st.button("Generate PDF Report", type="primary"):
            with st.spinner("Generating report..."):
                try:
                    res = requests.post(f"{API_URL}/api/report/generate")
                    if res.status_code == 200:
                        st.download_button("⬇️ Download Report", res.content, "OpenSight_Report.pdf", "application/pdf")
                except:
                    st.error("Report generation failed")
    
    with col_r2:
        st.image("https://via.placeholder.com/400x300?text=Report+Preview", use_container_width=True)
