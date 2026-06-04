import cv2

from app.detector import detect
from app.tracker import SimpleTracker

tracker = SimpleTracker()

video = cv2.VideoCapture(
    "data/videos/zone.mp4"
)
frame_count = 0
while True:

    ret, frame = video.read()
    frame_count += 1

    if frame_count % 5 != 0:
        continue

    if not ret:
        break

    detections = detect(frame)

    tracks = tracker.update(detections)

    for t in tracks:

        x1, y1, x2, y2 = map(int, t["bbox"])

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            str(t["id"]),
            (x1, y1),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0,255,0),
            2
        )

    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()