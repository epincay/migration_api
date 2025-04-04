# main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from core.database import engine, Base
from core.database import SessionLocal
from routers import quarterly_hires, dept_metrics, upload_departments, upload_jobs, upload_employees

app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine, checkfirst=True)  # Esto creará todas las tablas definidas en models.py

# Carga de departmets
app.include_router(upload_departments.router)    

# Carga de jobs
app.include_router(upload_jobs.router)    

# Carga de employees
app.include_router(upload_employees.router)    

# API quarterly_hires
app.include_router(quarterly_hires.router)    

# API dept_metrics
app.include_router(dept_metrics.router)