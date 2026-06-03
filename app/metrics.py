# app/metrics.py

import pandas as pd

def footfall(events):
    return len(events[events["event_type"]=="entry"])