@echo off
echo =====================================
echo      Starting ClassSense System
echo =====================================

cd /d %~dp0

echo Activating virtual environment...
call venv\Scripts\activate

echo Moving to Frontend folder...
cd Frontend

echo Starting Flask Server...
python server.py

pause