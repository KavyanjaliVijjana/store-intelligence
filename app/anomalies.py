def detect_anomalies(events):

    anomalies = []

    hourly = (
        events.groupby(
            events["event_timestamp"].str[:13]
        )
        .size()
    )

    avg = hourly.mean()

    for hour, count in hourly.items():

        if count > avg * 2:

            anomalies.append({
                "type": "crowd_spike",
                "hour": hour,
                "count": int(count)
            })

    return anomalies