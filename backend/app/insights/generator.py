import pandas as pd
from app.services.kpi_service import KPIService
from sqlalchemy.orm import Session

class InsightGenerator:
    def __init__(self, db: Session):
        self.db = db
        self.kpi_service = KPIService(db)

    def generate_insights(self):
        """
        Generate rule-based insights based on KPI data.
        """
        insights = []
        
        # Check for revenue drop
        daily_revenue = self.kpi_service.get_daily_revenue(days=14)
        if len(daily_revenue) >= 7:
            last_7_days = daily_revenue.tail(7)['revenue'].sum()
            prev_7_days = daily_revenue.head(7)['revenue'].sum()
            
            if prev_7_days > 0:
                drop_pct = (prev_7_days - last_7_days) / prev_7_days
                if drop_pct > 0.1:
                    insights.append({
                        "type": "revenue_drop",
                        "description": f"Revenue dropped by {drop_pct:.1%} in the last 7 days compared to the previous week.",
                        "suggested_action": "Check your ad campaigns and lead conversion funnel."
                    })
        
        # Check for channel performance
        channel_perf = self.kpi_service.get_conversion_by_channel()
        if not channel_perf.empty:
            best_channel = channel_perf.loc[channel_perf['revenue'].idxmax()]
            insights.append({
                "type": "best_channel",
                "description": f"The best performing channel is {best_channel['channel']} with ${best_channel['revenue']:.2f} in revenue.",
                "suggested_action": "Consider increasing ad spend on this channel."
            })
            
        # Default insight if none generated
        if not insights:
            insights.append({
                "type": "general",
                "description": "System is running smoothly. No significant anomalies detected.",
                "suggested_action": "Continue monitoring your daily metrics."
            })
            
        return insights
