from fastapi import UploadFile, File, APIRouter, Depends, HTTPException
from core.database import engine, Base
import csv
import io
from core.database import SessionLocal
import repositories.repositories as repositories
from datetime import datetime

router = APIRouter(prefix="", tags=["upload"])

# Endpoint subir archivos CSV a tabla employees    
@router.post("/upload/employees/")
async def upload_employees(file: UploadFile = File(...), batch_size: int = 100):
    try:
        contents = await file.read()
        text = contents.decode('utf-8')
        reader = csv.reader(io.StringIO(text))
        
        # Skip cabecera si existe
        # next(reader, None)
        
        employees = []
        for row in reader:
            if len(row) == 5:
                employees.append({"id": int(row[0]), "name": row[1], "date": datetime.fromisoformat(row[2].replace('Z', '+00:00')) if row[2].strip() else None, "department_id": int(row[3]) if row[3].strip() else 0, "job_id": int(row[4]) if row[4].strip() else 0})
        
        db = SessionLocal()
        try:
            for i in range(0, len(employees), batch_size):
                batch = employees[i:i + batch_size]
                repositories.create_employees(db, batch)
            return {"message": f"Successfully uploaded {len(employees)} employees"}
        finally:
            db.close()
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))