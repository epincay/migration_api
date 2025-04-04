from sqlalchemy import Column, Integer, String
from core.database import Base

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
