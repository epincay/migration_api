from sqlalchemy import Column, Integer, String, DateTime
from core.database import Base

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=True)
    date = Column(DateTime, unique=False, index=True)
    department_id = Column(Integer)
    job_id = Column(Integer)