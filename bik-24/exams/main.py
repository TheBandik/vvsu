from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')

class Task(BaseModel):
    title: str

tasks = []

@app.get('/', response_class=HTMLResponse)
def get_index(request: Request):
    return templates.TemplateResponse(
        'index.html',
        {'request': request, 'tasks': tasks}
    )

@app.post('/tasks', response_model=Task, status_code=201)
def create_task(request: Request, task_title: str = Form(...)):
    tasks.append(Task(title=task_title))
    return RedirectResponse(url="/", status_code=303)

@app.post('/tasks/delete/{task_id}', status_code=204)
def delete_task(task_id: int):
    if task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks.pop(task_id)
    return RedirectResponse(url="/", status_code=303)
