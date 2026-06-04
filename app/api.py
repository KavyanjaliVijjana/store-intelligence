from fastapi import FastAPI

from app.metrics import zone_visits
from app.events import load_events
from app.metrics import footfall, average_dwell_time, zone_visits
from app.anomalies import detect_anomalies
from app.sales_metrics import (
    load_sales_data,
    get_sales_metrics,
    conversion_rate
)

app = FastAPI(title="Purplle Store Intelligence")


@app.get("/")
def home():
    return {"status": "running"}


@app.get("/metrics")
def metrics():

    events = load_events(
        "data/events/generated.jsonl"
    )

    return {
        "footfall": footfall(events),
        "avg_dwell_seconds": average_dwell_time(events)
    }


@app.get("/funnel")
def funnel():

    events = load_events(
        "data/events/generated.jsonl"
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
        "data/events/generated.jsonl"
    )

    return detect_anomalies(events)

@app.get("/zones")
def zones():

    events = load_events(
        "data/events/generated.jsonl"
    )

    return zone_visits(events)

@app.get("/sales_metrics")
def sales_metrics():

    sales_df = load_sales_data(
        "data/sample_transactions.csv"
    )

    return get_sales_metrics(
        sales_df
    )

@app.get("/business_metrics")
def business_metrics():

    events = load_events(
        "data/events/generated.jsonl"
    )

    sales = load_sales_data(
        "data/sample_transactions.csv"
    )

    visitors = footfall(events)

    sales_data = get_sales_metrics(
        sales
    )

    sales_data["conversion_rate"] = (
        conversion_rate(
            visitors,
            sales_data["total_orders"]
        )
    )

    return sales_data