# app/events.py

import pandas as pd

def load_events(path):
    return pd.read_json(path, lines=True)


