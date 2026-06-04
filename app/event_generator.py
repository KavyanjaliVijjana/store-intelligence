import json
from datetime import datetime

def save_event(
    person_id,
    event_type,
    camera_id
):

    event = {
        "id_token": str(person_id),
        "event_type": event_type,
        "camera_id": camera_id,
        "event_timestamp": datetime.now().isoformat()
    }

    with open(
        "data/events/generated.jsonl",
        "a"
    ) as f:

        f.write(
            json.dumps(event) + "\n"
        )