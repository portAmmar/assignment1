from fastapi import FastAPI

app = FastAPI()

tasks = [
        {
                "id" : 1,
                "title" : "first task",
                "done" : false

            },{
                "id" : 2,
                "title" : "task 2",
                "done" : false
            },{
                "id" : 3,
                "title" : "task 3"
                "done" : false
            }
            ]

@app.get("/")
def read_root():
    return {
            "name":"Task API"
            "version":"1.0"
            "enpoints":["/tasks"]
            }

@app.get("health")
def test_server_health():
    return {"status": "ok"}

@app.get("/tasks")
def get_all_tasks():
    return tasks

@app.get("/task/{task_id}")
def get_task_by_id(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task

    return { "error": "Task 99 not found" }




