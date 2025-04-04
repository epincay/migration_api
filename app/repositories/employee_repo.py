from sqlalchemy.orm import Session
import models as models

def create_employees(db: Session, employees: list):
    db.bulk_insert_mappings(models.Employee, employees)
    db.commit()