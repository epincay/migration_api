# crud.py
from sqlalchemy.orm import Session
import models

# Funciones para insertar datos
def create_departments(db: Session, departments: list):
    db.bulk_insert_mappings(models.Department, departments)
    db.commit()

def create_jobs(db: Session, jobs: list):
    db.bulk_insert_mappings(models.Job, jobs)
    db.commit()

def create_hire_employees(db: Session, hire_employees: list):
    db.bulk_insert_mappings(models.Hire_Employees, hire_employees)
    db.commit()