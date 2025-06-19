import eel
from backend.listen import listen_command
from backend.speak import speak
from backend.system_control import open_app, close_app, get_time, get_date, set_alarm
from backend.web_search import open_website
#from backend.interaction import ask_groq

eel.init("frontend")  # Initialize with your frontend folder

def alarm_callback(msg):
    speak(msg)

@eel.expose
def handle_voice_command(command):
    command = command.lower()
    print(f"User said: {command}")

    if "exit" in command or "stop" in command:
        speak("Goodbye!")
        return "Session ended."
     
    elif " who is pragyan" in command or "who is gudu" in command:
         speak("pragyan is a most beatifull girl in your life to whom you love most and also he is always love you sir you both are looks love bird")
         return "Session ended."

    elif "something for pragyan" in command or "babe" in command:
         speak("hello pragyan mam i am assitant of ankit sir , ankit sir loves you most and always miss you , he may be sometime  on you but reason befine your love, love you by ankit sir")
         return "Session ended."
    
    elif open_app(command):
        speak("Opening application.")
        return "Opening application."

    elif "close" in command and close_app(command):
        speak("Closing application.")
        return "Closing application."

    elif open_website(command):
        speak("Opening website.")
        return "Opening website."

    elif "time" in command:
        result = get_time()
        speak(result)
        return result

    elif "date" in command:
        result = get_date()
        speak(result)
        return result

    elif "set alarm" in command:
        try:
            words = command.split("for")
            alarm_time = words[1].strip().upper()
            set_alarm(alarm_time, alarm_callback)
            speak(f"Alarm has been set for {alarm_time}")
            return f"Alarm has been set for {alarm_time}"
        except Exception:
            speak("Please say the time clearly, like 'set alarm for 6:30 AM'.")
            return "Please say the time clearly."

  #  else:
        #response = ask_groq(command)
        #speak(response)
        #return response
