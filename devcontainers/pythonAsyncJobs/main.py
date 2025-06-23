from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import redis
from pydantic import BaseModel
import uvicorn
from rq import Queue
import subprocess
import os

app = FastAPI()
r = redis.Redis(host='cache', port=6379, db=0)
queue = Queue(connection=r)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Event(BaseModel):
    event: str

def process_event(event: str):
    dir = "/workspace/.devcontainer"
    os.chdir(dir)

    command = "ls" 

    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    print("command output:")
    print(result.stdout)

    if result.stderr:
        print("Errors:")
        print(result.stderr)


@app.post("/events/")
async def create_event(event: Request):
    try:
        body = await event.json()
        print(f"Received event: {body}")
        headers = event.headers
        print(f"Headers: {headers}")
        if headers.get("x-github-event") == "push":
            job = queue.enqueue(process_event, "push")
            return ({"job_id": job.id, "status": "queued"}), 200
    except Exception as e:
        print(f"something went wrong: {e}")
        return {"status": "error", "message": "Invalid event but 200"}, 200

if __name__ == "__main__":
    uvicorn.run("main:app", log_level="info")