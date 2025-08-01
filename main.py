from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def serve_html():
    return FileResponse("index.html")

@app.get("/projects")
def get_projects():
    return {
        "projects": [
            {"id": 1, "name": "Proyecto A", "status": "active"},
            {"id": 2, "name": "Proyecto B", "status": "completed"},
            {"id": 3, "name": "Proyecto C", "status": "pending"}
        ]
    }
