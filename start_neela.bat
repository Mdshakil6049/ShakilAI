@echo off
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Age setup_windows.bat chalan.
    pause
    exit /b 1
)

".venv\Scripts\python.exe" main.py
pause