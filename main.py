# main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from database import engine, Base
import csv
import io
from typing import List
from database import SessionLocal
from datetime import datetime
import crud
import models
from sqlalchemy import extract, func, case, and_
from sqlalchemy.orm import Session
from pydantic import BaseModel

app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine, checkfirst=True)  # Esto creará todas las tablas definidas en models.py

# Endpoint subir archivos CSV a tabla departments
@app.post("/upload/departments/")
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
                crud.create_departments(db, batch)
            return {"message": f"Successfully uploaded {len(departments)} departments"}
        finally:
            db.close()
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint subir archivos CSV a tabla jobs
@app.post("/upload/jobs/")
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
                crud.create_jobs(db, batch)
            return {"message": f"Successfully uploaded {len(jobs)} jobs"}
        finally:
            db.close()
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint subir archivos CSV a tabla employees    
@app.post("/upload/employees/")
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
                crud.create_employees(db, batch)
            return {"message": f"Successfully uploaded {len(employees)} employees"}
        finally:
            db.close()
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    