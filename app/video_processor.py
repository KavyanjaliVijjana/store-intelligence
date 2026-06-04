import cv2

from app.zones import get_zone
from app.event_generator import save_event
from app.detector import model
from app.event_generator import save_event

video = cv2.VideoCapture("data/videos/zone.mp4")

seen_ids = set()
person_zones = {}
frame_count = 0

while True:

    ret, frame = video.read()

    if not ret:
        break

    frame_count += 1

    # Process every 2nd frame
    if frame_count % 2 != 0:
        continue

    results = model.track(
        frame,
        persist=True,
        classes=[0],
        verbose=False
    )

    if results[0].boxes.id is not None:

        boxes = results[0].boxes.xyxy.cpu().numpy()
        ids = results[0].boxes.id.cpu().numpy().astype(int)

        for box, person_id in zip(boxes, ids):

            x1, y1, x2, y2 = map(int, box)
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            zone = get_zone(center_x, center_y)

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"ID {person_id}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

            if person_id not in seen_ids:

                save_event(
                    person_id,
                    "entry",
                    "zone_cam"
                )

                seen_ids.add(person_id)
            
            previous_zone = person_zones.get(person_id)

            if zone is not None and zone != previous_zone:

                save_event(
                    person_id,
                    "zone_entered",
                    "zone_cam",
                    zone
                )

                person_zones[person_id] = zone

    cv2.imshow("Store Intelligence Tracking", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

video.release()
cv2.destroyAllWindows()