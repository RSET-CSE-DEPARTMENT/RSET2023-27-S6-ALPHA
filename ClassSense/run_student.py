#!/usr/bin/env python3
"""
ClassSense Student Launcher

Integrates Student App + Feature Extraction:
1. Launches the Python feature extraction module in the background
2. Optionally opens the meeting page in the browser

Usage:
  # After joining a session, run (get session + student ID from meeting URL):
  python run_student.py -s ABC123 -i <student-uuid>

  # Or let launcher open the meeting page for you:
  python run_student.py -s ABC123 -n "John" --open-browser

  # Headless mode (no OpenCV window, runs in background):
  python run_student.py -s ABC123 -i <student-uuid> --headless
"""
import argparse
import subprocess
import sys
import webbrowser
import uuid
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent
FEATURE_MAIN = PROJECT_ROOT / "feature" / "main.py"
BACKEND_URL = "http://127.0.0.1:5000"


def main():
    parser = argparse.ArgumentParser(
        description="ClassSense Student Launcher – starts feature extraction + optional browser"
    )
    parser.add_argument("-s", "--session", required=True, help="Session code (e.g. ABC123)")
    parser.add_argument("-i", "--student", help="Student ID (UUID). If omitted with --open-browser, generates one.")
    parser.add_argument("-n", "--name", default="Student", help="Student name (for browser URL)")
    parser.add_argument("-b", "--backend", default=BACKEND_URL, help="Backend URL")
    parser.add_argument("--headless", action="store_true", help="Run feature extraction without OpenCV window")
    parser.add_argument("--open-browser", action="store_true", help="Open meeting page in browser")
    parser.add_argument("--no-browser", action="store_true", help="Do not open browser (default when -i provided)")
    args = parser.parse_args()

    student_id = args.student
    if not student_id and args.open_browser:
        student_id = str(uuid.uuid4())
        print(f"Generated student ID: {student_id}")
        print("(Save this if you need to run the launcher again without --open-browser)")
    elif not student_id:
        print("Error: Provide -i/--student or use --open-browser to generate one.")
        sys.exit(1)

    if not FEATURE_MAIN.exists():
        print(f"Error: Feature module not found at {FEATURE_MAIN}")
        sys.exit(1)

    # Build feature extraction command
    cmd = [
        sys.executable,
        str(FEATURE_MAIN),
        "--session", args.session,
        "--student", student_id,
        "--backend", args.backend,
    ]
    if args.headless:
        cmd.append("--headless")

    if args.open_browser and not args.no_browser:
        url = f"{args.backend.rstrip('/')}/student/meeting.html"
        url += f"?code={args.session}&name={args.name}&id={student_id}"
        print(f"Opening {url}")
        webbrowser.open(url)

    print(f"Starting attention monitor (session={args.session}, student={student_id[:8]}...)")
    print("Press Ctrl+C to stop.")
    subprocess.run(cmd, cwd=str(PROJECT_ROOT))


if __name__ == "__main__":
    main()
