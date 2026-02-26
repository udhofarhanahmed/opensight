from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from datetime import datetime
from .base import Base

class SalesEvent(Base):
    __tablename__ = "sales_events"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, unique=True, index=True)
    customer_id = Column(String, index=True)
    product_id = Column(String, index=True)
    amount = Column(Float)
    currency = Column(String, default="USD")
    net_amount = Column(Float)  # Normalized to base currency
    channel = Column(String)  # Instagram, WhatsApp, Web, etc.
    status = Column(String)  # completed, pending, cancelled
    timestamp_utc = Column(DateTime, default=datetime.utcnow)
    raw_event_id = Column(Integer, ForeignKey("raw_events.id"))
