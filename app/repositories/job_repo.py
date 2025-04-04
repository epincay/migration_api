from sqlalchemy.orm import Session
import models as models

def create_jobs(db: Session, jobs: list):
    db.bulk_insert_mappings(models.Job, jobs)
    db.commit()
