import os
import time
import threading
from datetime import datetime

# 1. OPEN / CLOSE SYSTEM APPLICATIONS
def open_app(command):
    if "open notepad" in command:
        os.system("start notepad")
    elif "open calculator" in command:
        os.system("start calc")
    elif "open paint" in command:
        os.system("start mspaint")
    elif "open command prompt" in command or "open cmd" in command:
        os.system("start cmd")
    elif "open chrome" in command:
        os.system("start chrome")
    elif "open file explorer" in command:
        os.system("start explorer")
    else:
        return False
    return True

def close_app(command):
    if "close notepad" in command:
        os.system("taskkill /f /im notepad.exe")
    elif "close calculator" in command:
        os.system("taskkill /f /im calculator.exe")
    elif "close paint" in command:
        os.system("taskkill /f /im mspaint.exe")
    elif "close command prompt" in command or "close cmd" in command:
        os.system("taskkill /f /im cmd.exe")
    elif "close chrome" in command:
        os.system("taskkill /f /im chrome.exe")
    elif "close file explorer" in command:
        os.system("taskkill /f /im explorer.exe")
    else:
        return False
    return True

# 2. GET CURRENT TIME
def get_time():
    now = datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}."

# 3. GET CURRENT DATE
def get_date():
    now = datetime.now()
    return f"Today's date is {now.strftime('%A, %B %d, %Y')}."

# 4. SET ALARM (with callback to speak)
def set_alarm(alarm_time, callback):
    def alarm_thread():
        speak_msg = f"Alarm set for {alarm_time}"
        print(speak_msg)
        while True:
            current_time = datetime.now().strftime("%I:%M %p")
            if current_time == alarm_time:
                callback("⏰ Time to wake up!")
                break
            time.sleep(10)  # Check every 10 seconds
    threading.Thread(target=alarm_thread, daemon=True).start()
