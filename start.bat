@echo off
cd /d %~dp0

REM Start backend
start cmd /k "cd backend && venv\Scripts\activate && python manage.py runserver"

REM Start frontend (prevent browser)
start cmd /k "cd frontend && set BROWSER=none && npm start"

REM Wait 5 seconds for servers to be ready
timeout /t 5

REM Launch pywebview window
start cmd /k "cd backend && venv\Scripts\activate && cd .. && python start_webview.py"


