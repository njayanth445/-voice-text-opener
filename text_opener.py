import webbrowser
import subprocess
from datetime import datetime

print("=" * 60)
print("📱 TEXT COMMAND ASSISTANT 📱")
print("=" * 60)
print("Type any name and press Enter - it will open!")
print("")
print("Examples:")
print("  youtube     - Opens YouTube")
print("  google      - Opens Google")
print("  facebook    - Opens Facebook")
print("  calculator  - Opens Calculator")
print("  notepad     - Opens Notepad")
print("  time        - Shows current time")
print("  exit        - Stops program")
print("=" * 60)

# Database of websites
websites = {
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "facebook": "https://facebook.com",
    "fb": "https://facebook.com",
    "instagram": "https://instagram.com",
    "insta": "https://instagram.com",
    "twitter": "https://twitter.com",
    "x": "https://twitter.com",
    "github": "https://github.com",
    "git": "https://github.com",
    "amazon": "https://amazon.com",
    "netflix": "https://netflix.com",
    "spotify": "https://spotify.com",
    "gmail": "https://gmail.com",
    "mail": "https://gmail.com",
    "linkedin": "https://linkedin.com",
    "reddit": "https://reddit.com",
    "whatsapp": "https://web.whatsapp.com",
    "telegram": "https://web.telegram.org",
    "hotstar": "https://hotstar.com",
    "prime": "https://primevideo.com",
    "flipkart": "https://flipkart.com",
    "stackoverflow": "https://stackoverflow.com",
    "wikipedia": "https://wikipedia.org"
}

# Applications
apps = {
    "calculator": "calc.exe",
    "calc": "calc.exe",
    "notepad": "notepad.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "command": "cmd.exe",
    "powershell": "powershell.exe",
    "explorer": "explorer.exe"
}

def open_website(name):
    """Open any website"""
    name = name.lower().strip()
    
    # Check in database
    if name in websites:
        url = websites[name]
        webbrowser.open(url)
        print(f"✅ Opening {name}...")
        return True
    
    # Try adding .com
    try:
        url = f"https://{name}.com"
        webbrowser.open(url)
        print(f"✅ Opening {name}.com...")
        return True
    except:
        pass
    
    # Search Google
    print(f"🔍 Searching Google for '{name}'...")
    webbrowser.open(f"https://www.google.com/search?q={name}")
    return True

def open_app(name):
    """Open any application"""
    name = name.lower().strip()
    
    if name in apps:
        subprocess.Popen(apps[name], shell=True)
        print(f"✅ Opening {name}...")
        return True
    
    return False

def show_time():
    """Show current time"""
    now = datetime.now()
    print(f"🕐 Current time: {now.strftime('%I:%M:%S %p')}")
    print(f"📅 Date: {now.strftime('%B %d, %Y')}")

# Main loop
while True:
    # Get user input
    command = input("\n📝 Enter name: ").strip().lower()
    
    if not command:
        continue
    
    # Exit command
    if command in ["exit", "quit", "q", "close"]:
        print("👋 Goodbye!")
        break
    
    # Time command
    elif command in ["time", "date", "clock"]:
        show_time()
    
    # Help command
    elif command in ["help", "?", "commands", "list"]:
        print("\n📋 AVAILABLE COMMANDS:")
        print("   Websites: " + ", ".join(list(websites.keys())[:10]))
        print("   Apps: " + ", ".join(list(apps.keys())))
        print("   Special: time, date, help, exit")
    
    # Try opening as app first, then website
    elif open_app(command):
        pass
    
    else:
        open_website(command)