import pandas as pd
from sqlalchemy.orm import Session
from app.models.sales_event import SalesEvent
from sqlalchemy import func
from datetime import datetime, timedelta

class KPIService:
    def __init__(self, db: Session):
        self.db = db

    def get_daily_revenue(self, days: int = 30):
        """
        Get daily revenue for the last `days` days.
        """
        start_date = datetime.utcnow() - timedelta(days=days)
        
        # Query sales_events for daily revenue
        results = self.db.query(
            func.date(SalesEvent.timestamp_utc).label('day'),
            func.sum(SalesEvent.net_amount).label('revenue')
        ).filter(
            SalesEvent.timestamp_utc >= start_date,
            SalesEvent.status == 'completed'
        ).group_by('day').order_by('day').all()
        
        return pd.DataFrame(results, columns=['day', 'revenue'])

    def get_conversion_by_channel(self):
        """
        Get conversion rate by channel.
        For now, assume all sales_events are conversions.
        """
        results = self.db.query(
            SalesEvent.channel,
            func.count(SalesEvent.id).label('conversions'),
            func.sum(SalesEvent.net_amount).label('revenue')
        ).group_by(SalesEvent.channel).all()
        
        return pd.DataFrame(results, columns=['channel', 'conversions', 'revenue'])

    def get_summary_metrics(self):
        """
        Get high-level summary metrics.
        """
        total_revenue = self.db.query(func.sum(SalesEvent.net_amount)).filter(SalesEvent.status == 'completed').scalar() or 0.0
        total_orders = self.db.query(func.count(SalesEvent.id)).filter(SalesEvent.status == 'completed').scalar() or 0
        avg_order_value = total_revenue / total_orders if total_orders > 0 else 0.0
        
        return {
            "total_revenue": total_revenue,
            "total_orders": total_orders,
            "avg_order_value": avg_order_value
        }
