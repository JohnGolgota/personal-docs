from typing import Union
from fastapi import FastAPI
import redis
import time
import threading
from pydantic import BaseModel
import uvicorn

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, db=0)

class Event(BaseModel):
    event: str


def process_event(event: str):
    print(f"Processing event: {event}")
    time.sleep(10)
    print(f"Event processed: {event}")

def worker():
    while True:
        event = r.blpop("event_queue", timeout=0)
        if event:
            process_event(event[1].decode('utf-8'))


@app.post("/events/")
def create_event(event: Event):
    r.rpush("event_queue", event.event)
    return {"message": "Event added to queue"}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    threading.Thread(target=worker, daemon=True).start()
    uvicorn.run("main:app", log_level="info")