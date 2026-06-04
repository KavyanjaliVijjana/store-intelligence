from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect(frame):
    results = model.track(
        frame,
        persist=True,
        classes=[0],
        verbose=False
    )

    return results