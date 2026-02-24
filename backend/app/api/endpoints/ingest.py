from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
import pandas as pd
from io import StringIO
from sqlalchemy.orm import Session
from app.models.base import get_db
from app.models.raw import RawEvent

router = APIRouter()

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...), 
    mapping: str = None, # JSON string of mapping
    db: Session = Depends(get_db)
):
    import json
    filename = file.filename.lower()
    contents = await file.read()
    
    try:
        if filename.endswith('.csv'):
            df = pd.read_csv(StringIO(contents.decode('utf-8')))
        elif filename.endswith(('.xls', '.xlsx')):
            from io import BytesIO
            df = pd.read_excel(BytesIO(contents))
        else:
            raise HTTPException(400, "Only CSV or Excel files allowed")
    except Exception as e:
        raise HTTPException(400, f"Error reading file: {e}")
    
    # Apply mapping if provided
    if mapping:
        try:
            mapping_dict = json.loads(mapping)
            # Rename columns based on mapping
            # mapping_dict format: {"target_field": "source_column"}
            inv_map = {v: k for k, v in mapping_dict.items()}
            df = df.rename(columns=inv_map)
        except Exception as e:
            print(f"Mapping error: {e}")

    # Store raw data
    raw_records = df.to_dict(orient='records')
    for record in raw_records:
        raw_event = RawEvent(
            source=filename,
            data=record,
            status="pending"
        )
        db.add(raw_event)
    
    db.commit()
    return {"message": "File ingested", "rows": len(df)}
