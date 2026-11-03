@echo off
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" fuel_cost.py
) else (
    python fuel_cost.py
)
pause
