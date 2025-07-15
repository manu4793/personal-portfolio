import subprocess
import threading
import webview
import time

def run_backend():
    # Change this to your backend start command
    subprocess.Popen(['cmd', '/c', 'backend\\venv\\Scripts\\activate && python manage.py runserver'])

def run_frontend():
    # Change this to your frontend start command
    subprocess.Popen(['cmd', '/c', 'cd frontend && npm start'])

if __name__ == '__main__':
    # Start backend and frontend in background threads or subprocesses
    threading.Thread(target=run_backend).start()
    threading.Thread(target=run_frontend).start()

    # Wait a few seconds to let servers start
    time.sleep(10)

    # Open the app in a webview window
    webview.create_window('My Portfolio App', 'http://localhost:3000')
    webview.start()
