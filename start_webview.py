import webview
import time
import requests

url = 'http://localhost:3000'

def wait_for_server(url, timeout=30):
    start_time = time.time()
    while True:
        try:
            requests.get(url)
            return True
        except:
            if time.time() - start_time > timeout:
                return False
            time.sleep(1)

if wait_for_server(url):
    webview.create_window('My App', url)
    webview.start()
else:
    print("React server not responding.")
