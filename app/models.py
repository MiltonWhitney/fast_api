# app/models.py

#SQLALchemy imports
from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

# Define the Todo clase
class Todo(Base):
    # creating table name
    __tablename__ = "todos"

    # Defining columms for the table
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    
