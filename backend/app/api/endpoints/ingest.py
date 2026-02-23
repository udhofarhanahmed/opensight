from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
import pandas as pd
from io import StringIO
from sqlalchemy.orm import Session
from app.models.base import get_db
from app.models.raw import RawEvent

router = APIRouter()

@router.post("/csv")
async def ingest_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(400, "Only CSV files allowed")
    
    contents = await file.read()
    try:
        df = pd.read_csv(StringIO(contents.decode('utf-8')))
    except Exception as e:
        raise HTTPException(400, f"Error reading CSV: {e}")
    
    # Store raw data
    raw_records = df.to_dict(orient='records')
    for record in raw_records:
        raw_event = RawEvent(
            source="csv",
            data=record,
            status="pending"
        )
        db.add(raw_event)
    
    db.commit()
    return {"message": "File ingested", "rows": len(df)}
