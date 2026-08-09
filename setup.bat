@echo off
echo ============================================================
echo       Flora_AI Project Local Environment Setup (Windows)
echo ============================================================

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to PATH!
    echo Please install Python 3.10+ and add it to system PATH.
    pause
    exit /b 1
)

python setup.py

echo.
pause
