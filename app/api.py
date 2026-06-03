# # app/api.py

from fastapi import FastAPI

app = FastAPI(title="Purplle Store Intelligence")

@app.get("/")
def home():
    return {"status":"running"}

@app.get("/metrics")
def metrics():
    return {
        "footfall": 0,
        "avg_dwell_time": 0,
        "conversion_rate": 0
    }

from app.events import load_events
from app.metrics import footfall

@app.get("/metrics")
def metrics():

    events = load_events(
        "data/events/sample_events.jsonl"
    )

    return {
        "footfall": footfall(events)
    }