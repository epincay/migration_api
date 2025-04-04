from sqlalchemy.orm import Session
import models as models

# Funciones para insertar datos
def create_departments(db: Session, departments: list):
    db.bulk_insert_mappings(models.Department, departments)
    db.commit()
