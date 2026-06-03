from app.events import load_events

df = load_events("data/events/sample_events.jsonl")

print(df.head())