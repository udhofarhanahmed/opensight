import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from app.services.kpi_service import KPIService
from app.insights.generator import InsightGenerator
from app.models.base import SessionLocal

def generate_pdf_report(output_path: str, client_name: str = "OpenSight Demo"):
    """
    Generate a PDF report using WeasyPrint and Jinja2.
    """
    db = SessionLocal()
    try:
        kpi_service = KPIService(db)
        insight_gen = InsightGenerator(db)
        
        kpis = kpi_service.get_summary_metrics()
        insights = insight_gen.generate_insights()
        
        # Setup Jinja2
        template_dir = os.path.join(os.path.dirname(__file__), 'templates')
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template('report.html')
        
        # Render HTML
        html_out = template.render(
            client=client_name,
            logo="https://via.placeholder.com/150x50?text=OpenSight",
            kpis=kpis,
            insights=insights
        )
        
        # Generate PDF
        HTML(string=html_out).write_pdf(output_path)
        return output_path
    finally:
        db.close()

if __name__ == "__main__":
    generate_pdf_report("leakage_report.pdf")
