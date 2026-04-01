from ultralytics import YOLO

class YOLODetector:
    def __init__(self):
        # lightweight & fast
        self.model = YOLO("yolov8n.pt")

        # COCO class IDs
        self.PHONE_ID = 67   # cell phone
        self.PERSON_ID = 0

    def detect(self, frame):
        results = self.model(frame, verbose=False)[0]

        phone_detected = False
        person_count = 0

        if results.boxes is None:
            return phone_detected, person_count

        for box in results.boxes:
            cls = int(box.cls[0])

            if cls == self.PHONE_ID:
                phone_detected = True
            elif cls == self.PERSON_ID:
                person_count += 1

        return phone_detected, person_count
