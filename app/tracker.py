class SimpleTracker:

    def __init__(self):
        self.next_id = 1

    def update(self, detections):

        tracked = []

        for det in detections:

            tracked.append({
                "id": self.next_id,
                "bbox": det["bbox"]
            })

            self.next_id += 1

        return tracked