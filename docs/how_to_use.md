# 🌐 How to Use OpenSight as a Web App

OpenSight is designed to be used as a web application, accessible through your browser. Here's how you (the owner) and others can use it.

## 1. For the Owner (Local Access)
If you're running OpenSight on your own computer, you can access it locally:

1. **Start the System:**
   Open your terminal in the `opensight` folder and run:
   ```bash
   docker-compose -f infra/docker-compose.yml up --build
   ```
2. **Access the Dashboard:**
   Open your web browser and go to:
   `http://localhost:8501`
3. **Access the API (for developers):**
   Go to `http://localhost:8000/docs` to see the interactive API documentation.

---

## 2. For Others (Public Web Access)
To let others use OpenSight as a web app, you need to **deploy it to the cloud**. Once deployed, it will have a public URL (e.g., `https://your-opensight.render.com`).

### Recommended Free Cloud Options:
- **Render:** Great for hosting both the FastAPI backend and Streamlit dashboard.
- **Fly.io:** Offers a free tier for small applications.
- **Streamlit Community Cloud:** You can host the dashboard for free if your repository is on GitHub.

---

## 3. How to Use the App (Step-by-Step)

### Step 1: Ingest Data
1. Go to the **Data Ingestion** page in the sidebar.
2. Upload your sales data (CSV or Excel).
3. Click **Upload and Process**. The system will automatically clean the data and run the ETL pipeline.

### Step 2: Analyze Insights
1. Navigate to the **Dashboard** to see your total revenue, orders, and average order value.
2. View the **Revenue Trends & Forecast** chart to see historical performance and 30-day projections.
3. Check the **Insights** page for automated recommendations (e.g., revenue drops or best-performing channels).

### Step 3: Generate Reports
1. Go to the **Reports** page.
2. Click **Generate Report** to create a branded PDF summary of your sales intelligence.
3. Download the PDF to share with your team or clients.

---

## 4. Sharing with Others
Once your app is deployed to the cloud:
1. **Share the URL:** Simply send the public link to your team or clients.
2. **Multi-tenancy (Future):** Currently, the app is a single-tenant system. For multiple clients with isolated data, you can deploy separate instances or implement the `tenant_id` logic mentioned in the "Level Up" guide.
