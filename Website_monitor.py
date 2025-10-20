import time
import hashlib
import requests
import datetime
import webbrowser  

# URL of the page to monitor
url = "https://jeemain.nta.nic.in/"

# interval in seconds (e.g. 60 = check every 1 minute)
interval = 360  

def get_hash():
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return hashlib.sha256(response.text.encode('utf-8')).hexdigest()
    except Exception as e:
        print("Error fetching page:", e)
        return None

print(f"Monitoring {url} for changes...")
old_hash = get_hash()

while True:
    time.sleep(interval)
    new_hash = get_hash()
    
    if new_hash and old_hash and new_hash != old_hash:
        print(f"⚡ Page updated at {datetime.datetime.now()}! Results might be live now.")
        # Open in browser if desired:
        webbrowser.open(url)
        old_hash = new_hash
    else:
        print("No change yet...")