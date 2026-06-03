import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Purplle Store Intelligence",
    layout="wide"
)

st.title("🏬 Purplle Store Intelligence Dashboard")

metrics = requests.get(
    "http://127.0.0.1:8000/metrics"
).json()

funnel = requests.get(
    "http://127.0.0.1:8000/funnel"
).json()

anomalies = requests.get(
    "http://127.0.0.1:8000/anomalies"
).json()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Footfall",
        metrics["footfall"]
    )

with col2:
    st.metric(
        "Avg Dwell Time",
        metrics["avg_dwell_seconds"]
    )

st.divider()

st.subheader("Customer Funnel")

st.write(funnel)

st.divider()

st.subheader("Anomalies")

if len(anomalies):
    st.dataframe(
        pd.DataFrame(anomalies)
    )
else:
    st.success(
        "No anomalies detected"
    )