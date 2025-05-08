
import os
import subprocess
import time
import re
import json
import requests
import socket
import shutil
from datetime import datetime
import threading
import psutil

# Memory Directory (Safe User Directory)
MEMORY_DIR = os.path.expanduser("~/.lexar")
MEMORY_DB = os.path.join(MEMORY_DIR, "lexarv6_memory.json")
BACKUP_DIR = os.path.join(MEMORY_DIR, "backups")

def ensure_memory_directory():
    if not os.path.exists(MEMORY_DIR):
        os.makedirs(MEMORY_DIR)
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

def load_memory():
    ensure_memory_directory()
    if os.path.exists(MEMORY_DB):
        return restore_latest_backup()
    else:
        return {"commands": {}, "knowledge": pre_loaded_knowledge()}

def save_memory(memory_data):
    with open(MEMORY_DB, "w") as file:
        json.dump(memory_data, file, indent=4)

def pre_loaded_knowledge():
    return {
        "hello": "Hello, Michael! How can I help you today?",
        "what can you do": "I can secure your system, optimize it, manage your web panel, troubleshoot errors, teach you Linux, monitor your system, and much more.",
        "how do I secure my system": "I can set up a firewall, enable VPN, configure a secure proxy, and monitor your network.",
        "how do I optimize my PC": "I can clean your system, boost performance, manage startup apps, and optimize CPU and RAM usage.",
        "how's the weather": "Let me check the weather for your location.",
        "show my CPU usage": "I can display real-time CPU usage, memory usage, and other system metrics.",
        "what's my ip": "Sure, I can show your local and public IP addresses.",
        "search the web": "You can ask me to look up anything, and I will find the best answer for you.",
        "system status": "I can monitor your system in real-time, including CPU, RAM, Disk, and Network.",
        "linux help": "I can teach you Linux commands, how to use them, and help you troubleshoot any Linux system."
    }

# Initialize Memory Data
memory_data = load_memory()

def greeting():
    print('''
=================================================
 ██████╗ ██╗      █████╗ ██████╗  █████╗ ██████╗ 
██╔═══██╗██║     ██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║   ██║██║     ███████║██████╔╝███████║██║  ██║
██║   ██║██║     ██╔══██║██╔═══╝ ██╔══██║██║  ██║
╚██████╔╝███████╗██║  ██║██║     ██║  ██║██████╔╝
 ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═════╝ 
      LEXARV6 - THE ULTIMATE AI SYSTEM             
=================================================
''')
    print("Welcome, Michael! I’m Lexar, your limitless assistant. How can I help you today?")
    automatic_backup_scheduler()
    ai_chat_mode()

def ai_chat_mode():
    print("\n=== Conversational AI (Limitless Knowledge) ===")
    print("You can talk to me naturally, and I will always try to help.")
    print("(Type 'exit' to leave)")

    while True:
        user_input = input("Michael: ").lower()
        if "exit" in user_input:
            print("Goodbye, Michael. Have a great day!")
            save_memory(memory_data)
            break

        if "weather" in user_input:
            get_weather()
            continue

        if "ip" in user_input:
            show_ip_address()
            continue

        if "status" in user_input or "monitor" in user_input:
            system_status()
            continue

        if user_input in memory_data["knowledge"]:
            print(memory_data["knowledge"][user_input])
            continue

        if "search" in user_input or "look up" in user_input:
            search_query = user_input.replace("search", "").replace("look up", "").strip()
            web_search(search_query)
            continue

        print("Hmm, I'm not completely sure. Would you like me to search the web or help you troubleshoot?")
        choice = input("Search (web) / Troubleshoot: ").lower()
        if choice == "search":
            search_query = user_input.strip()
            web_search(search_query)
        elif choice == "troubleshoot":
            troubleshoot()
        else:
            print("Alright, let me know how else I can help.")

def system_status():
    print("🔍 System Status:")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"RAM Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
    print(f"Network Sent: {psutil.net_io_counters().bytes_sent / (1024 * 1024):.2f} MB")
    print(f"Network Received: {psutil.net_io_counters().bytes_recv / (1024 * 1024):.2f} MB")

def get_weather():
    print("Let me check the weather for your location...")
    try:
        ip_info = requests.get("https://ipinfo.io/").json()
        location = ip_info.get("city", "your location")
        response = requests.get(f"https://wttr.in/{location}?format=3")
        print(f"🌤 Weather in {location}: {response.text}")
    except:
        print("⚠️ I couldn't fetch the weather right now.")

def show_ip_address():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        public_ip = requests.get('https://api.ipify.org').text
        print(f"Local IP Address: {local_ip}")
        print(f"Public IP Address: {public_ip}")
    except:
        print("⚠️ Unable to retrieve IP address.")

def web_search(query):
    print(f"🔎 Searching the web for: {query}")
    response = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json")
    print("✅ Search Results:", response.json().get("AbstractText", "No clear answer found."))

def automatic_backup_scheduler():
    def backup_routine():
        while True:
            backup_memory()
            time.sleep(86400)

    backup_thread = threading.Thread(target=backup_routine, daemon=True)
    backup_thread.start()

def backup_memory():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"lexarv6_memory_backup_{timestamp}.json")
    shutil.copy(MEMORY_DB, backup_file)
    print(f"✅ Memory backed up at {backup_file}")

if __name__ == "__main__":
    greeting()
