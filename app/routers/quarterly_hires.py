from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, select, and_
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from models import Department, Employee, Job
from database import get_db
from pydantic import BaseModel
from database import SessionLocal
from sqlalchemy import extract, func, case, and_

router = APIRouter(prefix="", tags=["metrics"])

# Pydantic model for response
class QuarterlyHiresResponse(BaseModel):
    department: str
    job: str
    q1: int
    q2: int
    q3: int
    q4: int
    total: int

@router.get("/metrics/quarterly-hires/2021", 
            response_model=List[QuarterlyHiresResponse],
            summary="Empleados contratados por departamento",
            description="Lista de empleados contratados para cada puesto y departamento en 2021")
def get_quarterly_hires():
    db = SessionLocal()
    try:
        results = db.query(
            Department.name.label("department"),
            Job.title.label("job"),
            func.count(
                case((and_(
                    extract('year', Employee.date) == 2021,
                    extract('quarter', Employee.date) == 1
                ), 1), else_=None)
            ).label("q1"),
            func.count(
                case((and_(
                    extract('year', Employee.date) == 2021,
                    extract('quarter', Employee.date) == 2
                ), 1), else_=None)
            ).label("q2"),
            func.count(
                case((and_(
                    extract('year', Employee.date) == 2021,
                    extract('quarter', Employee.date) == 3
                ), 1), else_=None)
            ).label("q3"),
            func.count(
                case((and_(
                    extract('year', Employee.date) == 2021,
                    extract('quarter', Employee.date) == 4
                ), 1), else_=None)
            ).label("q4"),
            func.count().label("total")
        )\
        .join(Department, Employee.department_id == Department.id)\
        .join(Job, Employee.job_id == Job.id)\
        .filter(extract('year', Employee.date) == 2021)\
        .group_by(Department.name, Job.title)\
        .order_by(Department.name, Job.title)\
        .all()

        return [{
            "department": r.department,
            "job": r.job,
            "q1": r.q1,
            "q2": r.q2,
            "q3": r.q3,
            "q4": r.q4,
            "total": r.total
        } for r in results]
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()