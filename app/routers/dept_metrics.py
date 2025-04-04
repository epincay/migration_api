from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, select, and_
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from models import Department, Employee
from database import get_db
from pydantic import BaseModel

router = APIRouter(prefix="", tags=["metrics"])

class DepartmentHiringStats(BaseModel):
    id: int
    name: str
    employees_hired: int

@router.get("/metrics/above-average-hiring/2021", 
           response_model=List[DepartmentHiringStats],
           summary="Departamentos con contrataciones por encima de la media",
           description="Lista de departamentos que contrataron más empleados que el promedio de 2021")
def get_departments_above_average_hiring(db: Session = Depends(get_db)):
    try:
        # Subquery for hires per department
        dept_hires = (
            select(
                Department.id,
                Department.name,
                func.count(Employee.id).label("employees_hired")
            )
            .join(Employee, Department.id == Employee.department_id)
            .where(func.extract('year', Employee.date) == 2021)
            .group_by(Department.id, Department.name)
            .cte("dept_hires")
        )

        # Subquery for average hires
        avg_hires = (
            select(func.avg(dept_hires.c.employees_hired).label("avg_hires"))
            .select_from(dept_hires)
            .cte("avg_hires")
        )

        # Main query
        query = (
            select(
                dept_hires.c.id,
                dept_hires.c.name,
                dept_hires.c.employees_hired
            )
            .select_from(dept_hires, avg_hires)  # Sintaxis correcta para CROSS JOIN
            .where(dept_hires.c.employees_hired > avg_hires.c.avg_hires)
            .order_by(dept_hires.c.employees_hired.desc())
        )

        results = db.execute(query).all()
        
        return [{
            "id": r.id,
            "name": r.name,
            "employees_hired": r.employees_hired
        } for r in results]
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error calculating hiring metrics: {str(e)}"
        )