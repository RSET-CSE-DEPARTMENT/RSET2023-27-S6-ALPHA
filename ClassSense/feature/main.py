from modules.camera_capture import CameraCapture
from modules.vision_features import VisionFeatures
from modules.yolo_detector import YOLODetector
import cv2
import time
import argparse

try:
    import requests
except ImportError:
    requests = None


def send_metrics_to_backend(backend_url, session_code, student_id, metrics):
    """POST attention metrics to backend REST API."""
    if not requests or not backend_url or not session_code or not student_id:
        return
    url = f"{backend_url.rstrip('/')}/attention-metrics"
    payload = {
        "sessionCode": session_code,
        "studentId": student_id,
        "attentionScore": int(metrics.get("attention_score", 0)),
        "gaze": metrics.get("gaze", "CENTER"),
        "sleeping": metrics.get("sleeping", "NO"),
        "phone": metrics.get("phone", "NO"),
        "status": metrics.get("status", "FOCUSED"),
    }
    try:
        requests.post(url, json=payload, timeout=2)
    except Exception:
        pass


# -------------------- NEW FUNCTION --------------------
def check_if_student_active(backend_url, session_code, student_id):
    """Check if student is still active in the session."""
    if not requests:
        return True
    try:
        url = f"{backend_url.rstrip('/')}/my-attention?studentId={student_id}&sessionCode={session_code}"
        r = requests.get(url, timeout=2)

        if r.status_code != 200:
            return False

        data = r.json()

        # REQUIRED FIX: stop if backend marks student offline
        if data.get("status") == "offline":
            return False

        return True

    except Exception:
        return True


def draw_progress_bar(frame, score, x=15, y=45, w=300, h=18):
    cv2.rectangle(frame, (x, y), (x + w, y + h), (60, 60, 60), -1)
    filled_w = int((score / 100) * w)

    if score >= 70:
        color = (0, 200, 0)
    elif score >= 40:
        color = (0, 200, 200)
    else:
        color = (0, 0, 200)

    cv2.rectangle(frame, (x, y), (x + filled_w, y + h), color, -1)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 1)


def main(
    session_code=None,
    student_id=None,
    backend_url=None,
    headless=False,
):
    camera = CameraCapture()
    vision = VisionFeatures()
    yolo = YOLODetector()

    attention_score = 100

    last_score_update = time.time()

    # -------------------- NEW TIMER --------------------
    last_session_check = time.time()

    left_time = right_time = 0
    eye_off_time = 0
    phone_time = 0
    sleep_time = 0
    face_missing_time = 0

    api_mode = bool(session_code and student_id and backend_url)

    frame_count = 0
    cached_phone_visible = False
    cached_metrics = None

    try:
        while True:

            # -------------------- NEW SESSION CHECK --------------------
            if api_mode and time.time() - last_session_check > 3:
                last_session_check = time.time()
                if not check_if_student_active(backend_url, session_code, student_id):
                    print("Student left session. Stopping monitor.")
                    break
            # ----------------------------------------------------------

            frame = camera.get_frame()
            if frame is None:
                break

            frame_count += 1

            # Run vision (MediaPipe) every frame for smooth display, it's fast
            frame, metrics = vision.process_frame(frame)

            # Run YOLO only every 3rd frame to reduce lag
            if frame_count % 3 == 0:
                cached_phone_visible, _ = yolo.detect(frame)

            phone_visible = cached_phone_visible
            face_missing = metrics["penalty"] == 4

            using_phone = phone_visible or (
                metrics["gaze"] == "DOWN" and metrics["sleeping"] == "NO"
            )
            metrics["phone"] = "YES" if using_phone else "NO"

            now = time.time()
            if now - last_score_update >= 1.0:
                last_score_update = now

                if face_missing:
                    face_missing_time += 1
                else:
                    face_missing_time = 0

                left_time = left_time + 1 if metrics["gaze"] == "LEFT" else 0
                right_time = right_time + 1 if metrics["gaze"] == "RIGHT" else 0
                eye_off_time = eye_off_time + 1 if metrics["eye_focus"] == "OFF_SCREEN" else 0
                phone_time = phone_time + 1 if using_phone else 0
                sleep_time = sleep_time + 1 if metrics["sleeping"] == "YES" else 0

                if face_missing_time >= 2:
                    attention_score -= 3
                if face_missing_time >= 5:
                    attention_score -= 5

                if sleep_time > 0:
                    attention_score -= 6

                if phone_time > 0:
                    attention_score -= 4

                for t in (left_time, right_time):
                    if 2 <= t <= 5:
                        attention_score -= 0.5
                    elif t > 5:
                        attention_score -= 1.0

                if eye_off_time >= 2:
                    attention_score -= 1.5

                focus = (
                    not face_missing
                    and metrics["gaze"] == "CENTER"
                    and metrics["eye_focus"] == "ON_SCREEN"
                    and metrics["phone"] == "NO"
                    and metrics["sleeping"] == "NO"
                )

                if focus:
                    if attention_score < 40:
                        attention_score += 2
                    elif attention_score < 70:
                        attention_score += 1
                    else:
                        attention_score += 0.5

                attention_score = max(0, min(100, attention_score))

                if face_missing:
                    status, color = "ABSENT", (0, 0, 255)
                elif metrics["sleeping"] == "YES":
                    status, color = "SLEEPING", (0, 0, 255)
                elif using_phone:
                    status, color = "USING PHONE", (0, 0, 255)
                elif attention_score >= 70:
                    status, color = "FOCUSED", (0, 255, 0)
                elif attention_score >= 40:
                    status, color = "DISTRACTED", (0, 255, 255)
                else:
                    status, color = "NOT ATTENTIVE", (0, 0, 255)

                if api_mode:
                    send_metrics_to_backend(backend_url, session_code, student_id, {
                        "attention_score": attention_score,
                        "gaze": metrics["gaze"],
                        "sleeping": metrics["sleeping"],
                        "phone": metrics["phone"],
                        "status": status,
                    })

            if face_missing:
                status, color = "ABSENT", (0, 0, 255)
            elif metrics["sleeping"] == "YES":
                status, color = "SLEEPING", (0, 0, 255)
            elif using_phone:
                status, color = "USING PHONE", (0, 0, 255)
            elif attention_score >= 70:
                status, color = "FOCUSED", (0, 255, 0)
            elif attention_score >= 40:
                status, color = "DISTRACTED", (0, 255, 255)
            else:
                status, color = "NOT ATTENTIVE", (0, 0, 255)

            overlay = frame.copy()
            cv2.rectangle(overlay, (0, 0), (380, 220), (0, 0, 0), -1)
            frame = cv2.addWeighted(overlay, 0.6, frame, 0.4, 0)

            cv2.putText(frame, f"Attention Score: {int(attention_score)}",
                        (15, 28), cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (255, 255, 255), 2)

            draw_progress_bar(frame, attention_score)

            cv2.putText(frame, f"Gaze: {metrics['gaze']}", (15, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.65, (200, 200, 255), 2)

            cv2.putText(frame, f"Sleeping: {metrics['sleeping']}", (15, 110),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)

            if using_phone:
                cv2.putText(frame, "USING PHONE",
                            (15, 140), cv2.FONT_HERSHEY_SIMPLEX,
                            0.65, (0, 0, 255), 2)

            cv2.putText(frame, status, (400, 55),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, 3)

            if not headless:
                cv2.imshow("ClassSense – Attention Monitor", frame)
                cv2.waitKey(1)

    finally:
        camera.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ClassSense Attention Monitor")
    parser.add_argument("--session", "-s", help="Session code (enables API mode)")
    parser.add_argument("--student", "-i", help="Student ID (enables API mode)")
    parser.add_argument("--backend", "-b", default="http://127.0.0.1:5000",
                        help="Backend URL for REST API")
    parser.add_argument("--headless", action="store_true",
                        help="Run without OpenCV window (background mode)")
    args = parser.parse_args()

    main(
        session_code=args.session,
        student_id=args.student,
        backend_url=args.backend if (args.session and args.student) else None,
        headless=args.headless,
    )