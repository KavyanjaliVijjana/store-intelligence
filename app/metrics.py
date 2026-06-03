import pandas as pd

def footfall(events):
    return len(events[events["event_type"] == "entry"])


def average_dwell_time(events):

    entries = events[events["event_type"] == "entry"]
    exits = events[events["event_type"] == "exit"]

    dwell_times = []

    for person_id in entries["id_token"].unique():

        entry_row = entries[entries["id_token"] == person_id]

        exit_row = exits[exits["id_token"] == person_id]

        if len(entry_row) and len(exit_row):

            entry_time = pd.to_datetime(
                entry_row.iloc[0]["event_timestamp"]
            )

            exit_time = pd.to_datetime(
                exit_row.iloc[0]["event_timestamp"]
            )

            dwell = (exit_time - entry_time).total_seconds()

            dwell_times.append(dwell)

    if len(dwell_times) == 0:
        return 0

    return round(sum(dwell_times) / len(dwell_times), 2)