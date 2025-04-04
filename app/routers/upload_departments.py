from fastapi import UploadFile, File, APIRouter, Depends, HTTPException
from core.database import engine, Base
import csv
import io
from core.database import SessionLocal
import repositories.repositories as repositories


router = APIRouter(prefix="", tags=["upload"])

# Endpoint subir archivos CSV a tabla departments
@router.post("/upload/departments/")
async def upload_departments(file: UploadFile = File(...), batch_size: int = 100):
    try:
        contents = await file.read()
        text = contents.decode('utf-8')
        reader = csv.reader(io.StringIO(text))
        
        # Skip cabecera si existe
        # next(reader, None)
        
        departments = []
        for row in reader:
            if len(row) == 2:
                departments.append({"id": int(row[0]), "name": row[1]})
        
        db = SessionLocal()
        try:
            for i in range(0, len(departments), batch_size):
                batch = departments[i:i + batch_size]
                repositories.create_departments(db, batch)
            return {"message": f"Successfully uploaded {len(departments)} departments"}
        finally:
            db.close()
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))