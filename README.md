# OpenSight: Free & Open-Source Automated Sales Intelligence System (ASIS)

OpenSight is a modular sales analytics platform designed for SMEs. It ingests raw sales data, cleans it, computes key business metrics, and presents insights through an interactive dashboard and automated PDF reports.

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+

### Run with Docker
```bash
docker-compose -f infra/docker-compose.yml up --build
```
The dashboard will be available at `http://localhost:8501` and the API at `http://localhost:8000`.

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
