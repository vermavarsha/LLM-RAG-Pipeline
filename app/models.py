# app/models.py

from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    chunk_count = Column(Integer)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

engine = create_engine("sqlite:///metadata.db")
Base.metadata.create_all(engine)
