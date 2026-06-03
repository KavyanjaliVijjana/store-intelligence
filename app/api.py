from fastapi import FastAPI

from app.events import load_events
from app.metrics import footfall, average_dwell_time
from app.anomalies import detect_anomalies

app = FastAPI(title="Purplle Store Intelligence")


@app.get("/")
def home():
    return {"status": "running"}


@app.get("/metrics")
def metrics():

    events = load_events(
        "data/events/sample_events.jsonl"
    )

    return {
        "footfall": footfall(events),
        "avg_dwell_seconds": average_dwell_time(events)
    }


@app.get("/funnel")
def funnel():

    events = load_events(
        "data/events/sample_events.jsonl"
    )

    entered = len(
        events[events["event_type"] == "entry"]["id_token"].unique()
    )

    zone = len(
        events[events["event_type"] == "zone_entered"]["id_token"].unique()
    )

    exited = len(
        events[events["event_type"] == "exit"]["id_token"].unique()
    )

    return {
        "entered_store": entered,
        "visited_zone": zone,
        "exited_store": exited
    }


@app.get("/anomalies")
def anomalies():

    events = load_events(
        "data/events/sample_events.jsonl"
    )

    return detect_anomalies(events)