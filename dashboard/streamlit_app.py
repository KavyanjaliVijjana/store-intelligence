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

zones = requests.get(
    "http://127.0.0.1:8000/zones"
).json()

st.subheader("Zone Visits")

st.bar_chart(zones)

business = requests.get(
    "http://127.0.0.1:8000/business_metrics"
).json()

col3, col4, col5 = st.columns(3)

with col3:
    st.metric(
        "Revenue",
        f"₹{business['total_revenue']:,.0f}"
    )

with col4:
    st.metric(
        "Orders",
        business["total_orders"]
    )

with col5:
    st.metric(
        "Conversion %",
        business["conversion_rate"]
    )

st.subheader("Revenue vs Orders")

data = {
    "Metric": ["Revenue","Orders"],
    "Value": [
        business["total_revenue"],
        business["total_orders"]
    ]
}

st.bar_chart(
    pd.DataFrame(data)
    .set_index("Metric")
)