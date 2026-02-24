# ☁️ Cloud Deployment Guide (Free Tier)

To make OpenSight accessible as a web app for others, you can deploy it to a cloud provider. Here are the steps for **Render** and **Fly.io**.

## 1. Deploying to Render (Recommended)
Render is the easiest way to host both the FastAPI backend and the Streamlit dashboard for free.

### Step 1: Deploy the Backend (FastAPI)
1. Sign up for a free account at [Render](https://render.com).
2. Create a new **Web Service**.
3. Connect your GitHub repository (`udhofarhanahmed/opensight`).
4. Set the **Root Directory** to `backend`.
5. Set the **Build Command** to `pip install -r requirements.txt`.
6. Set the **Start Command** to `uvicorn app.main:app --host 0.0.0.0 --port 8000`.
7. Add an **Environment Variable**: `DATABASE_URL=sqlite:///./data.db`.

### Step 2: Deploy the Dashboard (Streamlit)
1. Create another **Web Service** on Render.
2. Connect the same GitHub repository.
3. Set the **Root Directory** to `app`.
4. Set the **Build Command** to `pip install -r requirements.txt`.
5. Set the **Start Command** to `streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0`.
6. Add an **Environment Variable**: `API_URL=https://your-backend-url.onrender.com`.

---

## 2. Deploying to Fly.io
Fly.io is another great option for hosting containerized applications.

1. Install the `flyctl` CLI on your computer.
2. Run `fly launch` in the `backend` folder to deploy the API.
3. Run `fly launch` in the `app` folder to deploy the Streamlit dashboard.
4. Follow the prompts to set up your app and environment variables.

---

## 3. Streamlit Community Cloud
If you only want to host the dashboard and have your API running elsewhere:
1. Go to [Streamlit Cloud](https://streamlit.io/cloud).
2. Connect your GitHub repo and select the `app/streamlit_app.py` file.
3. Set the `API_URL` in the **Secrets** section of your Streamlit app settings.

---

## 💡 Important Note on Free Tiers
- **Render's Free Tier:** The service will "sleep" after 15 minutes of inactivity. The first request after it sleeps will take about 30 seconds to wake up.
- **Fly.io:** Offers a small amount of free compute and storage, which is perfect for a demo or small business use.
