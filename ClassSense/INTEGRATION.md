# ClassSense Integration Guide

This document describes how the **Student App**, **Feature Extraction**, and **Backend** are integrated.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  STUDENT DEVICE (same machine)                                               │
│  ┌──────────────────────┐     subprocess      ┌───────────────────────────┐ │
│  │  Student App (HTML)   │ ─────────────────► │  Feature Extraction       │ │
│  │  meeting.html         │   run_student.py   │  Python (OpenCV, YOLO)    │ │
│  │  - Polls /my-attention│                    │  - Camera capture         │ │
│  │  - Shows real feedback│                    │  - Attention metrics      │ │
│  └──────────┬───────────┘                    └────────────┬──────────────┘ │
└─────────────┼─────────────────────────────────────────────┼────────────────┘
              │                                              │
              │ HTTP REST                                    │ HTTP POST
              │ (GET /my-attention)                          │ /attention-metrics
              ▼                                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  BACKEND (Flask + Firebase)                                                  │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  /attention-metrics (POST)  → Update Firestore session.students       │   │
│  │  /my-attention (GET)        → Return student's latest attention       │   │
│  │  /join-session, /heartbeat, /leave-session, /close-session            │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
              │
              │ Firestore real-time
              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  TEACHER DASHBOARD (HTML + Firebase)                                         │
│  - Live attention status per student                                         │
│  - Class analytics, heatmap, alerts                                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 1. Student App ↔ Feature Extraction

**Technology:** Python subprocess + REST trigger  
**How it works:** The student runs `run_student.py`, which launches the feature extraction module.

### Usage

After joining a session, the student opens a terminal and runs:

```bash
# From project root
python run_student.py -s ABC123 -i <student-uuid>
```

Or let the launcher generate a student ID and open the meeting page:

```bash
python run_student.py -s ABC123 -n "John" --open-browser
```

**Options:**
- `-s, --session` – Session code (required)
- `-i, --student` – Student UUID (required unless `--open-browser`)
- `-n, --name` – Student name (for browser URL)
- `--headless` – Run without OpenCV window (background mode)
- `--open-browser` – Open meeting page in browser

## 2. Feature Extraction → Backend

**Technology:** REST API (HTTP POST, JSON)  
**How it works:** Every second, the Python module POSTs metrics to `/attention-metrics`.

### Payload

```json
{
  "sessionCode": "ABC123",
  "studentId": "uuid-here",
  "attentionScore": 85,
  "gaze": "CENTER",
  "sleeping": "NO",
  "phone": "NO",
  "status": "FOCUSED"
}
```

### Feature Extraction CLI

```bash
cd feature
python main.py --session ABC123 --student <uuid> --backend http://127.0.0.1:5000 [--headless]
```

## 3. Backend Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/attention-metrics` | POST | Receive metrics from Python, update Firestore |
| `/my-attention` | GET | Return student's current attention (for meeting page) |
| `/join-session` | POST | Student joins session |
| `/leave-session` | POST | Student leaves session |
| `/heartbeat` | POST | Presence tracking |
| `/close-session` | POST | Teacher ends session |

## 4. Data Flow

1. **Student joins** via `index.html` → `/join-session` → Firestore
2. **Student runs** `run_student.py` → spawns `feature/main.py` with session + student ID
3. **Feature extraction** captures camera, computes attention, POSTs to `/attention-metrics` every 1s
4. **Backend** updates Firestore `sessions/<code>.students[i].attentionScore`
5. **Teacher dashboard** listens to Firestore → real-time attention updates
6. **Student meeting page** polls `/my-attention` every 2s → shows real feedback

## 5. Quick Start

1. Start the backend:
   ```bash
   cd Frontend && python server.py
   ```

2. Teacher: open http://127.0.0.1:5000 → Start session → share code

3. Student: open http://127.0.0.1:5000/student/ → Join with code

4. Student: in a terminal:
   ```bash
   python run_student.py -s <CODE> -i <ID> --open-browser
   ```
   (Code and ID are shown on the meeting page.)

5. Teacher: watch live attention on the dashboard
