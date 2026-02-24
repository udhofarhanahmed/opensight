# OpenSight: Free & Open-Source Automated Sales Intelligence System (ASIS)

OpenSight is a modular sales analytics platform designed for SMEs. It ingests raw sales data, cleans it, computes key business metrics, and presents insights through an interactive dashboard and automated PDF reports.

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+

## ✨ Enhanced Features (Level Up)
- **Advanced Ingestion:** Support for both CSV and Excel (.xlsx, .xls) files.
- **Live Exchange Rates:** Real-time currency normalization using live API data.
- **Data Quality:** Automated validation layer to catch missing or malformed data.
- **Fuzzy Deduplication:** Smart customer matching to handle near-duplicate entries.
- **Revenue Forecasting:** 30-day projections using Exponential Smoothing (Statsmodels).
- **Interactive Dashboard:** Date range filters and unified historical/forecast charts.

### Run with Docker
```bash
docker-compose -f infra/docker-compose.yml up --build
```
The dashboard will be available at `http://localhost:8501` and the API at `http://localhost:8000`.

## 🌐 How to Use as a Web App
OpenSight is designed to be used as a web application. You can access it in two ways:

1. **Local Access (Owner):** Run the system locally and access it at `http://localhost:8501`.
2. **Cloud Access (Others):** Deploy the system to a cloud provider like **Render** or **Fly.io** to get a public URL that others can use.

For detailed instructions, see:
- [How to Use Guide](docs/how_to_use.md)
- [Cloud Deployment Guide](docs/deploy_free.md)

### Local Development
1. Install backend dependencies:
   ```bash
   cd backend && pip install -r requirements.txt
   ```
2. Run the API:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Install dashboard dependencies:
   ```bash
   cd app && pip install -r requirements.txt
   ```
4. Run the dashboard:
   ```bash
   streamlit run streamlit_app.py
   ```

## 📂 Project Structure
- `backend/`: FastAPI application, ETL logic, and database models.
- `app/`: Streamlit dashboard.
- `report/`: PDF report generation logic and templates.
- `infra/`: Docker Compose configuration.
- `sample_data/`: Sample CSV data for testing.

## 🛠 Tech Stack
- **Backend:** FastAPI, SQLAlchemy, SQLite
- **ETL:** Pandas, Prefect
- **Dashboard:** Streamlit, Plotly
- **Reporting:** WeasyPrint, Jinja2

## 📄 License
This project is open-source and available under the MIT License.
