from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Task Management API is running"}

tasks = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Build first API", "completed": False}
]

"""CRUD - Understand the Concept 
CRUD is a software-development concept describing the four basic operations performed on 
application data. It is not a FastAPI feature.
CRUD Meaning
"""

# 1. READ operation - GET method
@app.get("/tasks")
def get_tasks():
    return tasks


# 2. CREATE operation - POST method
from fastapi import Body
@app.post("/tasks", status_code=201)
def create_task(task: dict = Body(...)):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.get("title", "Untitled task"),
        "completed": False
    }
    tasks.append(new_task)
    return new_task


# 3. UPDATE operation - PUT method
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: dict = Body(...)):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_data.get("title", task["title"])
            task["completed"] = task_data.get("completed", task["completed"])
            return task
    return {"message": "Task not found"}

# 4. DELETE operation - DELETE method
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}
    return {"message": "Task not found"}
