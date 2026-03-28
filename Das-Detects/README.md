# Das-Detects (Group 9)

A real-time AI voice detection system for VoIP calls. Das-Detects monitors active calls (e.g. WhatsApp) and classifies the caller's voice as **Human**, **Suspicious**, or **AI Generated** using a lightweight on-device CNN model paired with a GMM classifier. Detected scammer numbers are crowd-sourced to a shared blocklist via Supabase.

## Repository Structure

| Folder | Description |
|--------|-------------|
| `training/` | Model training pipeline — data preparation, feature extraction, CNN training, and TFLite conversion |
| `deployment/` | Desktop application — real-time audio capture, inference engine, UI, and cloud blocklist integration |

## How It Works

1. The app detects an active VoIP call via the Windows Audio Session API.
2. Audio is captured from the system loopback in ~2.5s frames.
3. Each frame is classified by two parallel models: a CNN (Mel Spectrogram + TFLite) and a GMM (LFCC features).
4. An ensemble decision engine smooths results over a rolling buffer and emits a final verdict.
5. If the caller's number is unsaved, it is hashed and checked against a Supabase blocklist. Confirmed AI callers are automatically reported.

## Getting Started

- To **run the app**, see [`deployment/README.md`](deployment/README.md).
- To **retrain the model**, see [`training/README.md`](training/README.md).

## Model Performance

| Metric | Value |
|--------|-------|
| Accuracy | 98.6% |
| Equal Error Rate (EER) | 1.75% |
| Inference Time | < 10ms |
| TFLite Model Size | ~87 KB |
