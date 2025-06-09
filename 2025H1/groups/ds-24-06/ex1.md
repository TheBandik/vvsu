```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []

class Task(BaseModel):
    title: str

@app.post('/tasks', response_model=Task)
def create_task(task: Task):
    tasks.append(task)

    return task

@app.get('/tasks/{task_id}', response_model=Task)
def get_task(task_id: int):
    if task_id >= len(tasks):
        raise HTTPException(status_code=404, detail='Task not found')
    
    return tasks[task_id]
```

```python
from typing import Annotated

from fastapi import FastAPI, Depends, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqladmin import Admin, ModelView

from database import engine, SessionLocal
import models.base as base
from models.user import User
import models.movie
import models.status
import models.genre
import models.user_movie

app = FastAPI()
admin = Admin(app, engine)

base.Base.metadata.create_all(bind=engine)

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username]

class UserBase(BaseModel):
    username: str
    password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post('/users/', status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    dump = user.model_dump()
    db_user = User(username=dump['username'])
    db_user.set_password(dump['password'])
    db.add(db_user)
    db.commit()

@app.post('/login')
async def login(user: UserBase, db: db_dependency):
    db_user = db.query(User).filter_by(username=user.username).first()
    if db_user:
        if db_user.check_password(user.password):
            return {
                "method": "/login",
                "status": "ok",
                "data": {
                    "username": user.username,
                    "status": True
                    }
                }
        else:
            return {
                "method": "/login",
                "status": "error",
                "data": {
                    "username": user.username,
                    "status": False
                    }
                }
    else:
        return {
                "method": "/login",
                "status": "error",
                "data": {
                    "username": user.username,
                    "status": False
                    }
                }

admin.add_view(UserAdmin)
```