from flask import Flask, request, jsonify, render_template, redirect, url_for, make_response
from flask_cors import CORS
import random
import string
import uuid
from datetime import datetime, timezone,timedelta
import csv
import io

import subprocess
import sys
from pathlib import Path

import firebase_admin
from firebase_admin import credentials, firestore, auth


# -------------------- APP SETUP --------------------
app = Flask(
    __name__,
    template_folder="teacher",
    static_folder="student_app",
    static_url_path="/student",
)
CORS(app)


# -------------------- FIREBASE SETUP --------------------
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


# -------------------- FEATURE MODULE PATH --------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
FEATURE_MAIN = PROJECT_ROOT / "feature" / "main.py"

# -------------------- NEW: PROCESS STORAGE --------------------
monitor_processes = {}


# -------------------- HELPERS --------------------
def generate_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


# -------------------- ROUTES --------------------
@app.route("/")
def root():
    return redirect(url_for("teacher_login"))

@app.route("/teacher/login.html")
@app.route("/teacher/login")
def teacher_login():
    return render_template("login.html")

@app.route("/teacher/subject_dashboard.html")
def subject_dashboard():
    return render_template("subject_dashboard.html")

@app.route("/teacher/class_dashboard.html")
def class_dashboard():
    return render_template("class_dashboard.html")

@app.route("/teacher")
def teacher():
    return redirect(url_for("teacher_login"))


@app.route("/api/teacher/delete", methods=["POST"])
def delete_teacher():
    data = request.json
    uid = data.get("uid")
    target_role = data.get("role")
    target_class = data.get("className")

    if not uid:
        return jsonify({"success": False, "error": "No UID provided"}), 400
    
    try:
        # 1. Target the specific role(s) to delete
        roles_query = db.collection("teacher_roles").where("uid", "==", uid)
        if target_role:
            roles_query = roles_query.where("role", "==", target_role)
        if target_class:
            roles_query = roles_query.where("class", "==", target_class)
            
        roles_to_delete = roles_query.get()
        for r in roles_to_delete:
            r.reference.delete()
            
        # 2. Check if the user has ANY roles left in the system
        remaining_roles = db.collection("teacher_roles").where("uid", "==", uid).get()
        
        # 3. If zero roles left, it's safe to completely delete their Firebase Auth user and Profile
        if len(remaining_roles) == 0:
            try:
                auth.delete_user(uid)
            except Exception:
                pass
            db.collection("teachers").document(uid).delete()
            
        return jsonify({"success": True, "completely_deleted": len(remaining_roles) == 0})
    except Exception as e:
        print(f"Error deleting teacher role/account: {e}")
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/start-session", methods=["POST"])
def start_session():
    data = request.get_json()
    teacher_uid = data.get("teacherUid", data.get("teacher")) # Fallback
    subject = data.get("subject", "General")
    class_name = data.get("className", "Unknown Class")

    session_code = generate_code()

    start_time = datetime.now(timezone.utc).isoformat()

    db.collection("sessions").document(session_code).set({
        "teacherUid": teacher_uid,
        "subject": subject,
        "className": class_name,
        "createdAt": start_time,
        "endedAt": None,
        "duration": None,
        "active": True,
        "students": []
    })

    return jsonify({"sessionCode": session_code})


@app.route("/join-session", methods=["POST"])
def join_session():
    data = request.json
    name = data["name"]
    student_id = data["studentId"]
    code = data["sessionCode"]

    doc_ref = db.collection("sessions").document(code)
    join_time = datetime.now().isoformat()

    @firestore.transactional
    def update_session(transaction):
        snapshot = doc_ref.get(transaction=transaction)
        if not snapshot.exists:
            return False

        session_data = snapshot.to_dict()

        if not session_data.get("active", True):
            return False

        students = session_data.get("students", [])

        student_exists = False
        for i, s in enumerate(students):
            if s.get("id") == student_id:
                students[i] = {
                    "id": student_id,
                    "name": name,
                    "joinTime": s.get("joinTime", join_time),
                    "lastSeen": join_time,
                    "status": "online"
                }
                student_exists = True
                break

        if not student_exists:
            students.append({
                "id": student_id,
                "name": name,
                "joinTime": join_time,
                "lastSeen": join_time,
                "status": "online",
                "leaveTime": None
            })

        transaction.update(doc_ref, {"students": students})
        return True

    transaction = db.transaction()
    try:
        joined = update_session(transaction)
        return jsonify({"joined": joined})
    except Exception as e:
        print(f"Transaction error: {e}")
        return jsonify({"joined": False, "error": str(e)}), 500


# -------------------- START MONITORING --------------------
@app.route("/start-monitoring", methods=["POST"])
def start_monitoring():
    data = request.json
    student_id = data.get("studentId")
    code = data.get("sessionCode")

    if not student_id or not code:
        return jsonify({"started": False}), 400

    cmd = [
        sys.executable,
        str(FEATURE_MAIN),
        "--session", code,
        "--student", student_id,
        "--backend", "http://127.0.0.1:5000"
    ]

    try:
        proc = subprocess.Popen(cmd, cwd=str(PROJECT_ROOT))

        # store process
        monitor_processes[student_id] = proc

        print(f"Started monitoring for student {student_id}")
        return jsonify({"started": True})
    except Exception as e:
        print(e)
        return jsonify({"started": False, "error": str(e)}), 500


@app.route("/leave-session", methods=["POST"])
def leave_session():
    data = request.json
    student_id = data["studentId"]
    code = data["sessionCode"]

    doc_ref = db.collection("sessions").document(code)
    leave_time = datetime.now().isoformat()

    @firestore.transactional
    def update_leave(transaction):
        snapshot = doc_ref.get(transaction=transaction)
        if not snapshot.exists:
            return False

        students = snapshot.to_dict().get("students", [])

        for i, s in enumerate(students):
            if s.get("id") == student_id:
                students[i] = {
                    **s,
                    "status": "offline",
                    "leaveTime": leave_time,
                    "lastSeen": leave_time
                }
                break

        transaction.update(doc_ref, {"students": students})
        return True

    transaction = db.transaction()

    try:
        left = update_leave(transaction)

        # Save meeting record for student
        student_ref = db.collection("Unq_Student").document(student_id)
        meetings_ref = student_ref.collection("meetings")

        # Derive alerts and durations from session data if available
        session_doc = doc_ref.get()
        session_data = session_doc.to_dict() if session_doc.exists else {}
        session_students = session_data.get("students", []) if session_data else []
        alerts_for_student = 0
        student_duration_min = data.get("studentDuration", 0)
        total_duration_min = data.get("totalDuration", 0)

        for s in session_students:
            if s.get("id") == student_id:
                alerts_for_student = int(s.get("alertsCount", 0) or 0)
                # If durations weren't sent from client, compute them here
                try:
                    created_at_str = session_data.get("createdAt")
                    if created_at_str and not total_duration_min:
                        created_dt = datetime.fromisoformat(created_at_str.replace("Z", ""))
                        ended_dt = datetime.fromisoformat(leave_time.replace("Z", ""))
                        total_duration_min = round(max(0, (ended_dt - created_dt).total_seconds()) / 60)
                    join_str = s.get("joinTime")
                    if join_str and not student_duration_min:
                        join_dt = datetime.fromisoformat(join_str.replace("Z", ""))
                        leave_dt = datetime.fromisoformat(leave_time.replace("Z", ""))
                        student_duration_min = round(max(0, (leave_dt - join_dt).total_seconds()) / 60)
                except Exception:
                    pass
                break

        docs = meetings_ref.stream()
        si_no = len(list(docs)) + 1

        meeting_data = {
            "Si_no": si_no,
            "Meet_id": code,
            "Teacher": data.get("teacher", session_data.get("teacherUid", "Unknown")),
            "Subject": session_data.get("subject", data.get("subject", "Unknown")),
            "Attention_score": data.get("attentionScore", 0),
            "Total_duration": total_duration_min,
            "Student_duration": student_duration_min,
            "Num_Alerts": alerts_for_student,
        }

        meetings_ref.document(str(si_no)).set(meeting_data)

        # Stop monitoring process
        proc = monitor_processes.get(student_id)
        if proc:
            try:
                proc.terminate()
                proc.wait(timeout=2)
                print(f"Stopped monitoring for student {student_id}")
            except Exception:
                pass
            monitor_processes.pop(student_id, None)

        return jsonify({"left": left})

    except Exception as e:
        print(f"Transaction error: {e}")
        return jsonify({"left": False, "error": str(e)}), 500


# -------------------- NEW: END SESSION --------------------
@app.route("/end-session", methods=["POST"])
def end_session():
    data = request.json
    code = data.get("sessionCode")

    doc_ref = db.collection("sessions").document(code)
    end_time = datetime.now(timezone.utc).isoformat()

    doc = doc_ref.get()
    if not doc.exists:
        return jsonify({"ended": False}), 404

    session_data = doc.to_dict()
    students = session_data.get("students", [])

    # Mark session inactive and store end time
    doc_ref.update({
        "active": False,
        "endedAt": end_time
    })

    # -------------------- SESSION HISTORY PERSISTENCE --------------------
    # Compute duration in seconds if we have a valid createdAt
    duration_seconds = None
    created_at_str = session_data.get("createdAt")
    try:
        if created_at_str:
            # Handle plain ISO strings
            created_dt = datetime.fromisoformat(created_at_str.replace("Z", ""))
            ended_dt = datetime.fromisoformat(end_time.replace("Z", ""))
            duration_seconds = int((ended_dt - created_dt).total_seconds())
    except Exception as e:
        print(f"Failed to compute duration for session {code}: {e}")

    # Aggregate student attention – use attentionHistory average if available (Issue #21)
    avg_attention = 0
    student_list = []
    student_ids = []
    if students:
        total_score = 0
        for s in students:
            # Compute average from history if available, else use snapshot
            history = s.get("attentionHistory", [])
            if history and len(history) > 0:
                score = round(sum(history) / len(history))
            else:
                score = int(s.get("attentionScore", 0) or 0)
            total_score += score
            sid = s.get("id")
            student_ids.append(sid)
            student_list.append({
                "id": sid,
                "name": s.get("name"),
                "attentionScore": score,
                "joinTime": s.get("joinTime"),
                "leaveTime": s.get("leaveTime"),
            })
        avg_attention = round(total_score / len(students))

    # Aggregate alerts, preferring live session data, with Unq_Student as fallback
    total_alerts = 0
    alerts_by_student = {}

    # First, use alertsCount stored in session students
    for s in students:
        sid = s.get("id")
        if not sid:
            continue
        ac = int(s.get("alertsCount", 0) or 0)
        alerts_by_student[sid] = ac
        total_alerts += ac

    # Fallback: pull from Unq_Student meetings when alertsCount not available
    try:
        meetings_query = db.collection_group("meetings").where("Meet_id", "==", code).get()
        for m in meetings_query:
            md = m.to_dict()
            num_alerts = int(md.get("Num_Alerts", 0) or 0)
            # Extract student id from path: Unq_Student/{sid}/meetings/{doc}
            try:
                sid_from_path = m.reference.parent.parent.id
            except Exception:
                sid_from_path = None
            if not sid_from_path:
                continue
            if sid_from_path not in alerts_by_student:
                alerts_by_student[sid_from_path] = num_alerts
                total_alerts += num_alerts
    except Exception as e:
        print(f"Failed to aggregate alerts for session {code}: {e}")

    history_doc = {
        "sessionId": code,
        "className": session_data.get("className"),
        "subject": session_data.get("subject"),
        "teacherUid": session_data.get("teacherUid"),
        "createdAt": session_data.get("createdAt"),
        "endedAt": end_time,
        "durationSeconds": duration_seconds,
        "averageAttention": avg_attention,
        "students": student_list,
        "studentIds": student_ids,
        "totalAlerts": total_alerts,
        "studentAlerts": alerts_by_student,
        "totalStudents": len(students),
        "active": False,
        "alertsSummary": {
            "totalCritical": data.get("totalCriticalAlerts", 0),
            "totalWarnings": data.get("totalWarningAlerts", 0),
            "totalRecoveries": data.get("totalRecoveries", 0),
            "alertsPausedDuringSession": data.get("alertsPaused", False),
        },
    }

    try:
        db.collection("session_history").document(code).set(history_doc)
    except Exception as e:
        print(f"Failed to write session_history for {code}: {e}")

    # -------------------- PER-STUDENT MEETING RECORDS (Unq_Student) --------------------
    # Ensure each student's meeting details are also stored/updated under Unq_Student
    try:
        for s in students:
            sid = s.get("id")
            if not sid:
                continue

            student_ref = db.collection("Unq_Student").document(sid)
            meetings_ref = student_ref.collection("meetings")

            # Ensure parent doc exists (but don't overwrite any existing data)
            try:
                if not student_ref.get().exists:
                    student_ref.set({"created": True}, merge=True)
            except Exception as e:
                print(f"Failed to ensure Unq_Student/{sid} exists: {e}")

            # Compute attention and durations from session data as a fallback
            attention_score = int(s.get("attentionScore", 0) or 0)
            alerts_for_student = int(alerts_by_student.get(sid, 0) or 0)

            student_join_str = s.get("joinTime")
            student_leave_str = s.get("leaveTime") or end_time

            student_duration_min = None
            total_duration_min = None
            try:
                if created_at_str and end_time:
                    created_dt = datetime.fromisoformat(created_at_str.replace("Z", ""))
                    ended_dt = datetime.fromisoformat(end_time.replace("Z", ""))
                    total_seconds = max(0, (ended_dt - created_dt).total_seconds())
                    total_duration_min = round(total_seconds / 60)

                if student_join_str and student_leave_str:
                    join_dt = datetime.fromisoformat(student_join_str.replace("Z", ""))
                    leave_dt = datetime.fromisoformat(student_leave_str.replace("Z", ""))
                    student_seconds = max(0, (leave_dt - join_dt).total_seconds())
                    student_duration_min = round(student_seconds / 60)
            except Exception as e:
                print(f"Failed to compute durations for student {sid} in session {code}: {e}")

            # Try to find an existing meeting doc for this session
            existing_docs = meetings_ref.where("Meet_id", "==", code).limit(1).get()
            if existing_docs:
                m_ref = existing_docs[0].reference
                current = existing_docs[0].to_dict() or {}
                update_payload = {}

                if "Attention_score" not in current or not current.get("Attention_score"):
                    update_payload["Attention_score"] = attention_score

                if student_duration_min is not None and (
                    "Student_duration" not in current or not current.get("Student_duration")
                ):
                    update_payload["Student_duration"] = student_duration_min

                if total_duration_min is not None and (
                    "Total_duration" not in current or not current.get("Total_duration")
                ):
                    update_payload["Total_duration"] = total_duration_min

                if "Subject" not in current or not current.get("Subject"):
                    update_payload["Subject"] = session_data.get("subject", "Unknown")

                if "Teacher" not in current or not current.get("Teacher"):
                    update_payload["Teacher"] = session_data.get("teacher", "Unknown")

                if "Num_Alerts" not in current or current.get("Num_Alerts") in (None, 0):
                    update_payload["Num_Alerts"] = alerts_for_student

                if update_payload:
                    try:
                        m_ref.update(update_payload)
                    except Exception as e:
                        print(f"Failed to update meeting doc for student {sid} in session {code}: {e}")
            else:
                # Create a new meeting entry if none exists for this session
                try:
                    all_docs = list(meetings_ref.stream())
                    si_no = len(all_docs) + 1
                except Exception:
                    si_no = 1

                meeting_data = {
                    "Si_no": si_no,
                    "Meet_id": code,
                    "Teacher": session_data.get("teacher", "Unknown"),
                    "Subject": session_data.get("subject", "Unknown"),
                    "Attention_score": attention_score,
                    "Total_duration": total_duration_min or 0,
                    "Student_duration": student_duration_min or 0,
                    "Num_Alerts": alerts_for_student,
                }

                try:
                    meetings_ref.document(str(si_no)).set(meeting_data)
                except Exception as e:
                    print(f"Failed to create meeting doc for student {sid} in session {code}: {e}")
    except Exception as e:
        print(f"Failed to sync Unq_Student records for session {code}: {e}")

    # stop all monitoring processes
    for s in students:
        sid = s.get("id")
        proc = monitor_processes.get(sid)

        if proc:
            try:
                proc.terminate()
                proc.wait(timeout=2)
                print(f"Stopped monitoring for {sid}")
            except Exception:
                pass

            monitor_processes.pop(sid, None)

    return jsonify({"ended": True})


@app.route("/attention-metrics", methods=["POST"])
def attention_metrics():
    data = request.json
    if not data:
        return jsonify({"updated": False}), 400

    student_id = data.get("studentId")
    code = data.get("sessionCode")
    attention_score = data.get("attentionScore", 0)
    status = data.get("status")

    doc_ref = db.collection("sessions").document(code)
    current_time = datetime.now().isoformat()

    @firestore.transactional
    def update_metrics(transaction):
        snapshot = doc_ref.get(transaction=transaction)
        if not snapshot.exists:
            return False

        students = snapshot.to_dict().get("students", [])

        for i, s in enumerate(students):
            if s.get("id") == student_id:
                prev_status = s.get("status")
                prev_alerts = int(s.get("alertsCount", 0) or 0)

                def is_alert_state(st):
                    return st in ("NOT ATTENTIVE", "DISTRACTED", "USING PHONE", "SLEEPING", "ABSENT")

                alerts = prev_alerts
                if status is not None and is_alert_state(status) and not is_alert_state(prev_status):
                    alerts += 1

                students[i] = {
                    **s,
                    "attentionScore": int(min(100, max(0, attention_score))),
                    "lastSeen": current_time,
                    "status": status or s.get("status", "online"),
                    "alertsCount": alerts,
                    "attentionHistory": (s.get("attentionHistory") or []) + [int(min(100, max(0, attention_score)))],
                }
                break

        transaction.update(doc_ref, {"students": students})
        return True

    transaction = db.transaction()
    updated = update_metrics(transaction)
    return jsonify({"updated": updated})


# -------------------- MODIFIED ROUTE --------------------
@app.route("/my-attention", methods=["GET"])
def my_attention():
    student_id = request.args.get("studentId")
    code = request.args.get("sessionCode")

    doc = db.collection("sessions").document(code).get()

    if not doc.exists:
        return jsonify({"error": "Session not found"}), 404

    session_data = doc.to_dict()

    # NEW: detect if teacher ended session
    if not session_data.get("active", True):
        return jsonify({"error": "Session ended"}), 404

    students = session_data.get("students", [])

    for s in students:
        if s.get("id") == student_id:

            if s.get("status") == "offline":
                return jsonify({"error": "Student offline"}), 404

            return jsonify({
                "attentionScore": s.get("attentionScore")
            })

    return jsonify({"error": "Student not in session"}), 404


# -------------------- ANALYTICS API --------------------
@app.route("/api/analytics/class", methods=["GET"])
def analytics_class():
    """
    Returns aggregated analytics for a class (and optional subject) based on session_history.
    Query params:
        teacherUid (optional)
        className (optional)
        subject (optional)
    """
    teacher_uid = request.args.get("teacherUid")
    class_name = request.args.get("className")
    subject = request.args.get("subject")

    try:
        query = db.collection("session_history")
        if teacher_uid:
            query = query.where("teacherUid", "==", teacher_uid)
        if class_name:
            query = query.where("className", "==", class_name)
        if subject:
            query = query.where("subject", "==", subject)

        # Fetch and sort in-memory to avoid composite index requirements
        docs = query.stream()

        sessions = []
        for d in docs:
            item = d.to_dict()
            item["id"] = d.id
            sessions.append(item)

        sessions.sort(key=lambda s: (s.get("createdAt") or s.get("endedAt") or ""))

        total_sessions = len(sessions)
        summary = {
            "totalSessions": total_sessions,
            "averageAttention": None,
            "bestSession": None,
            "worstSession": None,
        }

        if total_sessions > 0:
            attentions = [int(s.get("averageAttention", 0) or 0) for s in sessions]
            summary["averageAttention"] = round(sum(attentions) / len(attentions))
            summary["bestSession"] = max(attentions)
            summary["worstSession"] = min(attentions)

        return jsonify({"sessions": sessions, "summary": summary})

    except Exception as e:
        print(f"analytics_class error: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/analytics/session/<session_id>", methods=["GET"])
def analytics_session(session_id):
    """
    Returns detailed analytics for a single completed session from session_history.
    """
    try:
        doc = db.collection("session_history").document(session_id).get()
        if not doc.exists:
            return jsonify({"error": "Session not found"}), 404
        data = doc.to_dict()
        data["id"] = doc.id
        return jsonify(data)
    except Exception as e:
        print(f"analytics_session error: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/analytics/student", methods=["GET"])
def analytics_student():
    """
    Returns attention trend for a student across sessions from session_history.
    Query params:
        studentId (required)
        className (optional)
        subject (optional)
        teacherUid (optional)
    """
    student_id = request.args.get("studentId")
    if not student_id:
        return jsonify({"error": "studentId is required"}), 400

    class_name = request.args.get("className")
    subject = request.args.get("subject")
    teacher_uid = request.args.get("teacherUid")

    try:
        query = db.collection("session_history").where("studentIds", "array_contains", student_id)
        if teacher_uid:
            query = query.where("teacherUid", "==", teacher_uid)
        if class_name:
            query = query.where("className", "==", class_name)
        if subject:
            query = query.where("subject", "==", subject)

        docs = query.stream()

        history = []
        for d in docs:
            data = d.to_dict()
            # Find this student's score in the session
            score = 0
            for s in data.get("students", []):
                if s.get("id") == student_id:
                    score = int(s.get("attentionScore", 0) or 0)
                    break
            history.append({
                "sessionId": d.id,
                "createdAt": data.get("createdAt"),
                "averageAttention": data.get("averageAttention", 0),
                "studentAttention": score,
                "className": data.get("className"),
                "subject": data.get("subject"),
            })

        history.sort(key=lambda h: (h.get("createdAt") or ""))

        return jsonify({"studentId": student_id, "history": history})

    except Exception as e:
        print(f"analytics_student error: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/<code>")
def meeting(code):
    return render_template("meeting.html")


@app.route("/teacher/class_analytics.html")
def class_analytics():
    return render_template("class_analytics.html")


@app.route("/api/analytics/session/<session_id>/download", methods=["GET"])
def download_session_report(session_id):
    """
    Download a CSV report for a single session from session_history.
    """
    try:
        doc = db.collection("session_history").document(session_id).get()
        if not doc.exists:
            return jsonify({"error": "Session not found"}), 404

        data = doc.to_dict()
        students = data.get("students", [])

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["Student ID", "Name", "Attention Score", "Join Time", "Leave Time"])

        for s in students:
            writer.writerow([
                s.get("id") or "",
                s.get("name") or "",
                s.get("attentionScore", 0),
                s.get("joinTime") or "",
                s.get("leaveTime") or "",
            ])

        csv_content = output.getvalue()
        response = make_response(csv_content)
        response.headers["Content-Type"] = "text/csv"
        response.headers["Content-Disposition"] = f"attachment; filename=session_{session_id}.csv"
        return response
    except Exception as e:
        print(f"download_session_report error: {e}")
        return jsonify({"error": str(e)}), 500


# -------------------- RUN --------------------
if __name__ == "__main__":
    app.run(debug=True)