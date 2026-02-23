import pandas as pd
from sqlalchemy.orm import Session
from app.models.sales_event import SalesEvent
from sqlalchemy import func
from datetime import datetime, timedelta
import numpy as np
try:
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
except ImportError:
    ExponentialSmoothing = None

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

    def get_revenue_forecast(self, forecast_days: int = 30):
        """
        Generate revenue forecast for the next `forecast_days` days.
        """
        df = self.get_daily_revenue(days=90)
        if df.empty or len(df) < 7 or ExponentialSmoothing is None:
            return pd.DataFrame()
        
        # Prepare data for forecasting
        df['day'] = pd.to_datetime(df['day'])
        df = df.set_index('day').asfreq('D').fillna(0)
        
        try:
            # Simple Exponential Smoothing
            model = ExponentialSmoothing(df['revenue'], seasonal='add', seasonal_periods=7).fit()
            forecast = model.forecast(forecast_days)
            
            forecast_df = pd.DataFrame({
                'day': [df.index[-1] + timedelta(days=i+1) for i in range(forecast_days)],
                'revenue': forecast.values
            })
            return forecast_df
        except Exception as e:
            print(f"Forecasting error: {e}")
            return pd.DataFrame()
