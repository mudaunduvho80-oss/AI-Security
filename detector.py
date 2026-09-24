from ultralytics import YOLO
from config import CONFIDENCE_THRESHOLD, PERSON_CLASS

# Load the YOLO model
model = YOLO("yolo26n.pt")


def detect_person(frame):

    results = model(
        frame,
        conf=CONFIDENCE_THRESHOLD,
        verbose=False
    )

    person_detected = False

    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            if class_name == PERSON_CLASS:
                person_detected = True

    return person_detected, results