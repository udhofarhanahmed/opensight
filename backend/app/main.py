from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.api.endpoints import ingest
from app.services.kpi_service import KPIService
from app.insights.generator import InsightGenerator
from app.models.base import get_db, engine, Base
from app.etl.flows.main_flow import etl_pipeline
import os

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="OpenSight API")

# Include routers
app.include_router(ingest.router, prefix="/api/ingest", tags=["ingestion"])

@app.get("/api/kpis/summary")
def get_kpi_summary(db: Session = Depends(get_db)):
    kpi_service = KPIService(db)
    return kpi_service.get_summary_metrics()

@app.get("/api/kpis/daily")
def get_daily_revenue(db: Session = Depends(get_db), days: int = 30):
    kpi_service = KPIService(db)
    df = kpi_service.get_daily_revenue(days=days)
    return df.to_dict(orient='records')

@app.get("/api/kpis/forecast")
def get_revenue_forecast(db: Session = Depends(get_db), days: int = 30):
    kpi_service = KPIService(db)
    df = kpi_service.get_revenue_forecast(forecast_days=days)
    return df.to_dict(orient='records')

@app.get("/api/insights")
def get_insights(db: Session = Depends(get_db)):
    insight_gen = InsightGenerator(db)
    return insight_gen.generate_insights()

@app.post("/api/etl/run")
def run_etl():
    etl_pipeline()
    return {"message": "ETL pipeline executed"}

@app.post("/api/report/generate")
def generate_report():
    from report.generate_report import generate_pdf_report
    report_path = "opensight_report.pdf"
    generate_pdf_report(report_path)
    return FileResponse(report_path, media_type="application/pdf", filename="opensight_report.pdf")

@app.get("/")
def read_root():
    return {"message": "Welcome to OpenSight API"}
