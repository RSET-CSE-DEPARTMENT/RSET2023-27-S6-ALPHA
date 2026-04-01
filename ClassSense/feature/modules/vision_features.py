import cv2
import mediapipe as mp
import numpy as np
import math
from collections import deque


class VisionFeatures:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=3,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        self.EAR_THRESHOLD = 0.23
        self.MAR_THRESHOLD = 0.6
        self.PHONE_PITCH_THRESHOLD = 32

        self.eye_closed_frames = 0
        self.down_frames = 0
        self.prev_face_area = None

        # 👁 Eye landmarks
        self.LEFT_EYE = [33, 160, 158, 133, 153, 144]
        self.RIGHT_EYE = [362, 385, 387, 263, 373, 380]

        # 👁 Iris landmarks
        self.LEFT_IRIS = [468, 469, 470, 471]
        self.RIGHT_IRIS = [473, 474, 475, 476]

        self.MOUTH = [61, 81, 13, 311, 291, 308, 402, 14]

        # 🧠 Eye focus stability
        self.eye_focus_history = deque(maxlen=12)

    # ---------- helpers ----------
    def eye_aspect_ratio(self, eye):
        v1 = np.linalg.norm(eye[1] - eye[5])
        v2 = np.linalg.norm(eye[2] - eye[4])
        h = np.linalg.norm(eye[0] - eye[3])
        return (v1 + v2) / (2.0 * h)

    def mouth_aspect_ratio(self, mouth):
        v = np.linalg.norm(mouth[1] - mouth[7])
        h = np.linalg.norm(mouth[0] - mouth[4])
        return v / h

    def face_area(self, face):
        xs = [lm.x for lm in face.landmark]
        ys = [lm.y for lm in face.landmark]
        return (max(xs) - min(xs)) * (max(ys) - min(ys))

    def face_center_distance(self, face):
        cx = sum(lm.x for lm in face.landmark) / len(face.landmark)
        cy = sum(lm.y for lm in face.landmark) / len(face.landmark)
        return abs(cx - 0.5) + abs(cy - 0.5)

    def head_pitch(self, face):
        nose = face.landmark[1]
        chin = face.landmark[152]
        return math.degrees(math.atan2(chin.y - nose.y, chin.x - nose.x))

    # ---------- main ----------
    def process_frame(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)

        metrics = {
            "gaze": "CENTER",
            "eye_focus": "ON_SCREEN",
            "yawning": "NO",
            "sleeping": "NO",
            "phone": "NO",
            "attentive": False,
            "penalty": 0
        }

        if not results.multi_face_landmarks:
            metrics["penalty"] = 4
            return frame, metrics

        face = sorted(
            results.multi_face_landmarks,
            key=lambda f: (-self.face_area(f), self.face_center_distance(f))
        )[0]

        # ---------- 👁 EYES ----------
        left_eye = [np.array([face.landmark[i].x, face.landmark[i].y]) for i in self.LEFT_EYE]
        right_eye = [np.array([face.landmark[i].x, face.landmark[i].y]) for i in self.RIGHT_EYE]

        ear = (self.eye_aspect_ratio(left_eye) + self.eye_aspect_ratio(right_eye)) / 2
        is_blinking = ear < self.EAR_THRESHOLD

        if is_blinking:
            self.eye_closed_frames += 1
        else:
            self.eye_closed_frames = 0

        # 😴 Sleeping (long eye closure)
        if self.eye_closed_frames > 35:
            metrics["sleeping"] = "YES"
            metrics["penalty"] += 6
            return frame, metrics

        # ---------- 😮 YAWNING ----------
        mouth = [np.array([face.landmark[i].x, face.landmark[i].y]) for i in self.MOUTH]
        if self.mouth_aspect_ratio(mouth) > self.MAR_THRESHOLD:
            metrics["yawning"] = "YES"
            metrics["penalty"] += 3

        # ---------- 👤 HEAD GAZE ----------
        xs = [lm.x for lm in face.landmark]
        rel_x = (face.landmark[1].x - min(xs)) / (max(xs) - min(xs) + 1e-6)

        if rel_x < 0.32:
            metrics["gaze"] = "LEFT"
            metrics["penalty"] += 2
        elif rel_x > 0.68:
            metrics["gaze"] = "RIGHT"
            metrics["penalty"] += 2

        # ---------- 👀 EYE FOCUS (BLINK-SAFE) ----------
        if not is_blinking and metrics["gaze"] == "CENTER":
            left_iris_x = np.mean([face.landmark[i].x for i in self.LEFT_IRIS])
            right_iris_x = np.mean([face.landmark[i].x for i in self.RIGHT_IRIS])

            left_eye_left = face.landmark[33].x
            left_eye_right = face.landmark[133].x
            right_eye_left = face.landmark[362].x
            right_eye_right = face.landmark[263].x

            left_ratio = (left_iris_x - left_eye_left) / (left_eye_right - left_eye_left + 1e-6)
            right_ratio = (right_iris_x - right_eye_left) / (right_eye_right - right_eye_left + 1e-6)

            eye_focus_ratio = (left_ratio + right_ratio) / 2
            self.eye_focus_history.append(eye_focus_ratio)

            if len(self.eye_focus_history) >= 8:
                variation = max(self.eye_focus_history) - min(self.eye_focus_history)
                if variation > 0.04:
                    metrics["eye_focus"] = "OFF_SCREEN"
                    metrics["penalty"] += 2
        else:
            # do NOT corrupt history during blink
            self.eye_focus_history.clear()

        # ---------- 📱 PHONE ----------
        pitch = self.head_pitch(face)

        eye_y = (face.landmark[33].y + face.landmark[263].y) / 2
        face_center_y = np.mean([lm.y for lm in face.landmark])
        looking_down = eye_y > face_center_y + 0.015

        area = self.face_area(face)
        area_drop = self.prev_face_area and area < self.prev_face_area * 0.75
        self.prev_face_area = area

        if pitch > self.PHONE_PITCH_THRESHOLD and looking_down and area_drop:
            self.down_frames += 1
            if self.down_frames > 8:
                metrics["phone"] = "YES"
                metrics["gaze"] = "DOWN"
                metrics["penalty"] += 5
        else:
            self.down_frames = 0

        if metrics["penalty"] == 0:
            metrics["attentive"] = True

        return frame, metrics
