from typing import Union
from fastapi import FastAPI
import redis
import time
import threading
from pydantic import BaseModel
import uvicorn
from rq import Queue

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, db=0)
queue = Queue(connection=r)

class Event(BaseModel):
    event: str

def process_event(event: str):
    print(f"Processing event: {event}")
    time.sleep(10)
    print(f"Event processed: {event}")

@app.post("/events/")
def create_event(event: Event):
    job = queue.enqueue(process_event, event.event)
    return ({"job_id": job.id, "status": "queued"}), 200

if __name__ == "__main__":
    uvicorn.run("main:app", log_level="info")