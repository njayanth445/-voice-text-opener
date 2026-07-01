import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import os
from datetime import datetime
import requests
import json

print("=" * 70)
print("🎤 UNIVERSAL VOICE ASSISTANT - Opens ANYTHING! 🎤")
print("=" * 70)
print("You can open any website, app, or do many tasks!")
print("=" * 70)

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume', 0.9)

# Database of websites and apps (Easily expandable)
WEBSITES = {
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "github": "https://github.com",
    "gmail": "https://mail.google.com",
    "facebook": "https://facebook.com",
    "twitter": "https://twitter.com",
    "instagram": "https://instagram.com",
    "linkedin": "https://linkedin.com",
    "reddit": "https://reddit.com",
    "amazon": "https://amazon.com",
    "flipkart": "https://flipkart.com",
    "netflix": "https://netflix.com",
    "hotstar": "https://hotstar.com",
    "spotify": "https://spotify.com",
    "whatsapp": "https://web.whatsapp.com",
    "telegram": "https://web.telegram.org",
    "stackoverflow": "https://stackoverflow.com",
    "wikipedia": "https://wikipedia.org",
    "bing": "https://bing.com",
    "yahoo": "https://yahoo.com",
}

APPLICATIONS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "command prompt": "cmd.exe",
    "powershell": "powershell.exe",
    "explorer": "explorer.exe",
    "file explorer": "explorer.exe",
    "task manager": "taskmgr.exe",
    "control panel": "control.exe",
    "snipping tool": "SnippingTool.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "powerpoint": "powerpnt.exe",
    "outlook": "outlook.exe",
    "chrome": "chrome.exe",
    "firefox": "firefox.exe",
    "edge": "msedge.exe",
    "spotify": "spotify.exe",
    "discord": "discord.exe",
    "telegram": "Telegram.exe",
    "whatsapp": "WhatsApp.exe",
    "vscode": "code.exe",
    "visual studio code": "code.exe",
    "pycharm": "pycharm64.exe",
    "intellij": "idea64.exe",
}

def speak(text):
    """Convert text to speech"""
    print(f"\n🤖 Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for voice commands"""
    try:
        with sr.Microphone() as source:
            print("\n🎤 Listening... (Say a command)")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
        
        print("🔄 Processing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"✅ You said: '{command}'")
        return command
        
    except sr.UnknownValueError:
        print("❌ Could not understand")
        return ""
    except sr.RequestError:
        print("❌ Check internet")
        return ""
    except sr.WaitTimeoutError:
        print("⏰ No speech detected")
        return ""
    except Exception as e:
        print(f"❌ Error: {e}")
        return ""

def open_website(site_name):
    """Open any website"""
    site_name = site_name.lower().strip()
    
    # Check if in database
    for key, url in WEBSITES.items():
        if key in site_name or site_name in key:
            webbrowser.open(url)
            speak(f"Opening {key}")
            return True
    
    # Try to open as custom URL
    if "." in site_name:
        url = f"https://{site_name}" if not site_name.startswith("http") else site_name
        webbrowser.open(url)
        speak(f"Opening {site_name}")
        return True
    
    # Search Google if not found
    speak(f"I don't have {site_name} saved. Searching Google...")
    webbrowser.open(f"https://www.google.com/search?q={site_name}")
    return True

def open_application(app_name):
    """Open any application"""
    app_name = app_name.lower().strip()
    
    # Check in database
    for key, path in APPLICATIONS.items():
        if key in app_name or app_name in key:
            try:
                subprocess.Popen(path, shell=True)
                speak(f"Opening {key}")
                return True
            except:
                pass
    
    # Try to open as direct command
    try:
        subprocess.Popen(app_name, shell=True)
        speak(f"Opening {app_name}")
        return True
    except:
        pass
    
    # Search in Program Files
    common_paths = [
        f"C:\\Program Files\\{app_name.title()}\\{app_name}.exe",
        f"C:\\Program Files (x86)\\{app_name.title()}\\{app_name}.exe",
        f"C:\\Program Files\\{app_name.title()}\\bin\\{app_name}.exe",
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            subprocess.Popen(path)
            speak(f"Opening {app_name}")
            return True
    
    speak(f"Could not find {app_name}")
    return False

def search_web(query):
    """Search Google for anything"""
    speak(f"Searching Google for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def tell_time():
    """Tell current time"""
    now = datetime.now()
    time_str = now.strftime("%I:%M %p")
    speak(f"The time is {time_str}")

def tell_date():
    """Tell current date"""
    now = datetime.now()
    date_str = now.strftime("%B %d, %Y")
    speak(f"Today is {date_str}")

def get_weather(city="your city"):
    """Get weather (requires API key for full features)"""
    speak("Opening weather information")
    webbrowser.open(f"https://www.google.com/search?q=weather")

def send_email():
    """Open email"""
    webbrowser.open("https://mail.google.com")
    speak("Opening Gmail")

def take_note():
    """Open notepad for taking notes"""
    subprocess.Popen("notepad.exe")
    speak("Opening notepad for notes")

def shutdown_system():
    """Shutdown computer"""
    speak("Are you sure you want to shutdown? Say yes to confirm")
    confirm = listen()
    if confirm and "yes" in confirm:
        speak("Shutting down system")
        os.system("shutdown /s /t 5")
    else:
        speak("Shutdown cancelled")

def restart_system():
    """Restart computer"""
    speak("Are you sure you want to restart? Say yes to confirm")
    confirm = listen()
    if confirm and "yes" in confirm:
        speak("Restarting system")
        os.system("shutdown /r /t 5")
    else:
        speak("Restart cancelled")

# Welcome message
speak("Universal Assistant Activated!")
speak("I can open any website, any application, search the web, tell time, and much more!")

# Main loop
while True:
    command = listen()
    
    if not command:
        continue
    
    # Exit commands
    if any(word in command for word in ["exit", "quit", "stop", "goodbye", "bye"]):
        speak("Goodbye! Have a great day!")
        break
    
    # System commands
    elif "shutdown" in command or "turn off" in command:
        shutdown_system()
    
    elif "restart" in command:
        restart_system()
    
    # Time and date
    elif "time" in command and "what" in command:
        tell_time()
    
    elif "date" in command:
        tell_date()
    
    # Search commands
    elif "search" in command or "google" in command:
        query = command.replace("search", "").replace("google", "").strip()
        if query:
            search_web(query)
        else:
            speak("What would you like to search for?")
            query = listen()
            if query:
                search_web(query)
    
    # Open website (generic)
    elif "open" in command or "launch" in command or "go to" in command:
        # Extract what to open
        what = command.replace("open", "").replace("launch", "").replace("go to", "").strip()
        
        if what:
            # Check if it's a website
            if any(ext in what for ext in [".com", ".org", ".net", ".in", "youtube", "google", "facebook"]):
                open_website(what)
            else:
                # Try opening as app first, then website
                if not open_application(what):
                    open_website(what)
    
    # Direct website mentions
    elif any(site in command for site in WEBSITES.keys()):
        open_website(command)
    
    # Direct app mentions
    elif any(app in command for app in APPLICATIONS.keys()):
        open_application(command)
    
    # Weather
    elif "weather" in command:
        get_weather()
    
    # Email
    elif "email" in command or "mail" in command:
        send_email()
    
    # Notes
    elif "note" in command or "memo" in command:
        take_note()
    
    # Help
    elif "help" in command or "what can you do" in command:
        speak("I can open any website like YouTube, Google, Facebook. I can open apps like Notepad, Calculator, Chrome. I can search Google, tell time and date, send emails, take notes, shutdown or restart computer. Just say open followed by the name!")
    
    # Unknown command - try to intelligently handle
    else:
        # Try to interpret as something to open
        if len(command.split()) <= 3:
            speak(f"Try saying 'open {command}' to open that")
        else:
            speak("I didn't understand. Say 'help' to see what I can do")

print("\n" + "=" * 70)
print("Assistant stopped. Run again with: python universal_assistant.py")
print("=" * 70)