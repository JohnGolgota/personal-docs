from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import redis
import time
from pydantic import BaseModel
import uvicorn
from rq import Queue

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
    print(f"Processing event: {event}")
    time.sleep(10)
    print(f"Event processed: {event}")

@app.post("/events/")
async def create_event(event: Request):
    try:
        body = await event.json()
        print(f"Received event: {body}")
        headers = event.headers
        print(f"Headers: {headers}")
    except Exception as e:
        print(f"Error parsing JSON: {e}")
    finally:
        job = queue.enqueue(process_event, "push")
        return ({"job_id": job.id, "status": "queued"}), 200

if __name__ == "__main__":
    uvicorn.run("main:app", log_level="info")