#app/main.py

## FastAPI imports
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from .models import Todo

# Calling Models database library
models.Base.metadata.create_all(bind=Engine)

#attaching app variable to FastApi
app = FastApi(title="FastApi Todo App")

# creating class Todo
class TodoCreate(BaseModel):
    title: str
    description: str | None = none

class TodoRead(TodoCreate):
    id: int
    class Config:
        orm_mode = True
    
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Todo"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/todos/", response_model=TodoRead)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = models.Todo(title=todo.title, description=todo.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return todo

@app.get("/todos/", response_model=List[TodoRead])
def list_todo(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()

@app.delete("/todo/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, details="Todo not found")
    db.delete(todo)
    db.commit()
    return {"deleted": todo_id}






