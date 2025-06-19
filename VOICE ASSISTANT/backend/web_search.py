import webbrowser

def open_website(command):
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com")
    elif "open github" in command:
        webbrowser.open("https://www.github.com")
    elif "open stack overflow" in command or "open stackoverflow" in command:
        webbrowser.open("https://stackoverflow.com")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
    elif "open twitter" in command or "open x" in command:
        webbrowser.open("https://twitter.com")
    elif "open whatsapp" in command or "open whatsapp web" in command:
        webbrowser.open("https://web.whatsapp.com")
    elif "open netflix" in command:
        webbrowser.open("https://www.netflix.com")
    elif "open amazon" in command:
        webbrowser.open("https://www.amazon.in")
    elif "open flipkart" in command:
        webbrowser.open("https://www.flipkart.com")
    elif "open spotify" in command:
        webbrowser.open("https://www.spotify.com")
    elif "open google maps" in command or "open maps" in command:
        webbrowser.open("https://www.google.com/maps")
    elif "open youtube music" in command:
        webbrowser.open("https://music.youtube.com")
    elif "open wikipedia" in command:
        webbrowser.open("https://www.wikipedia.org")
    else:
        return False
    return True
