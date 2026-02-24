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

    def get_summary_metrics(self, days: int = 30):
        """
        Get high-level summary metrics with period comparison.
        """
        # Current period
        start_date = datetime.utcnow() - timedelta(days=days)
        
        # Previous period for comparison
        prev_start_date = start_date - timedelta(days=days)
        
        def get_metrics(start, end):
            query = self.db.query(
                func.sum(SalesEvent.net_amount).label('revenue'),
                func.count(SalesEvent.id).label('orders')
            ).filter(
                SalesEvent.timestamp_utc >= start,
                SalesEvent.timestamp_utc < end,
                SalesEvent.status == 'completed'
            ).first()
            
            revenue = query.revenue or 0.0
            orders = query.orders or 0
            aov = revenue / orders if orders > 0 else 0.0
            return revenue, orders, aov

        curr_rev, curr_ord, curr_aov = get_metrics(start_date, datetime.utcnow())
        prev_rev, prev_ord, prev_aov = get_metrics(prev_start_date, start_date)
        
        def calc_change(curr, prev):
            if prev == 0: return 0.0
            return ((curr - prev) / prev) * 100

        return {
            "total_revenue": curr_rev,
            "total_orders": curr_ord,
            "avg_order_value": curr_aov,
            "revenue_change": calc_change(curr_rev, prev_rev),
            "orders_change": calc_change(curr_ord, prev_ord),
            "aov_change": calc_change(curr_aov, prev_aov)
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
