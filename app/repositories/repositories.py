# crud.py
from sqlalchemy.orm import Session
import models as models

# Funciones para insertar datos
def create_departments(db: Session, departments: list):
    db.bulk_insert_mappings(models.Department, departments)
    db.commit()

def create_jobs(db: Session, jobs: list):
    db.bulk_insert_mappings(models.Job, jobs)
    db.commit()

def create_employees(db: Session, employees: list):
    db.bulk_insert_mappings(models.Employee, employees)
    db.commit()