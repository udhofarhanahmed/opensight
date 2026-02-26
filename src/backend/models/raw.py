from sqlalchemy import Column, Integer, JSON, DateTime, String
from datetime import datetime
from .base import Base

class RawEvent(Base):
    __tablename__ = "raw_events"
    
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String)  # e.g., 'csv', 'gsheets'
    data = Column(JSON)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="pending")  # pending, processed, failed
