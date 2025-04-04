import json
import requests
import time
import os

# ✅ Define your Slack webhook URL here
WEBHOOK_URL = 'https://hooks.slack.com/services/REPLACE/ME/WITH/REAL_URL'

# ✅ Define the correct path to Cowrie's log file
LOG_FILE = '/home/cowrie/cowrie/var/log/cowrie/cowrie.log'

def send_to_slack(message):
    payload = {'text': message}
    headers = {'Content-Type': 'application/json'}
    try:
        requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
    except Exception as e:
        print(f"Slack send failed: {e}")

def follow(logfile):
    logfile.seek(0, os.SEEK_END)
    while True:
        line = logfile.readline()
        if not line:
            time.sleep(0.2)
            continue
        yield line

# ✅ Start monitoring the Cowrie log
try:
    with open(LOG_FILE, 'r') as f:
        loglines = follow(f)
        for line in loglines:
            line = line.strip()
            if "login attempt" in line:
                send_to_slack(f"🔐 Login Attempt: {line}")
            elif "CMD:" in line:
                send_to_slack(f"💻 Command Executed: {line}")
            elif "download:" in line:
                send_to_slack(f"📥 File Download Attempt: {line}")
            elif "New connection" in line:
                send_to_slack(f"🔌 New Session Started: {line}")
            elif "connection lost" in line:
                send_to_slack(f"📴 Session Ended: {line}")
except FileNotFoundError:
    print(f"❌ Log file not found: {LOG_FILE}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
