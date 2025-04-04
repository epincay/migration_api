from fastapi import UploadFile, File, APIRouter, Depends, HTTPException
from core.database import engine, Base
import csv
import io
from core.database import SessionLocal
import repositories.job_repo as repositories


router = APIRouter(prefix="", tags=["upload"])

# Endpoint subir archivos CSV a tabla jobs
@router.post("/upload/jobs/")
async def upload_jobs(file: UploadFile = File(...), batch_size: int = 100):
    try:
        contents = await file.read()
        text = contents.decode('utf-8')
        reader = csv.reader(io.StringIO(text))
        
        # Skip cabecera si existe
        # next(reader, None)
        
        jobs = []
        for row in reader:
            if len(row) == 2:
                jobs.append({"id": int(row[0]), "title": row[1]})
        
        db = SessionLocal()
        try:
            for i in range(0, len(jobs), batch_size):
                batch = jobs[i:i + batch_size]
                repositories.create_jobs(db, batch)
            return {"message": f"Successfully uploaded {len(jobs)} jobs"}
        finally:
            db.close()
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))