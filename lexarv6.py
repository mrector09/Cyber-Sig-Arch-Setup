
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
MAX_BACKUPS = 10

def ensure_memory_directory():
    if not os.path.exists(MEMORY_DIR):
        os.makedirs(MEMORY_DIR)
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    manage_backups()  # Manage backups on startup

def load_memory():
    ensure_memory_directory()
    if os.path.exists(MEMORY_DB):
        return restore_latest_backup()
    else:
        return {"commands": {}, "knowledge": pre_loaded_knowledge()}

def save_memory(memory_data):
    with open(MEMORY_DB, "w") as file:
        json.dump(memory_data, file, indent=4)
    backup_memory()

def pre_loaded_knowledge():
    return {
        "hello": "Hello, Michael! How can I help you today?",
        "what can you do": "I can secure systems, write code, troubleshoot errors, teach you Linux, monitor your system, and much more.",
        "how do I secure my system": "I can set up a firewall, enable VPN, configure a secure proxy, and monitor your network.",
        "how do I write code": "I can write, debug, and explain code in Python, Bash, JavaScript, and more.",
        "how do I troubleshoot errors": "I can diagnose system issues, repair broken services, and help fix any problems you encounter.",
        "optimize my PC": "I can clean your system, boost performance, manage startup apps, and optimize CPU and RAM usage.",
        "show my CPU usage": "I can display real-time CPU usage, memory usage, and other system metrics.",
        "search the web": "You can ask me to look up anything, and I will find the best answer for you."
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
    print("Welcome, Michael! I’m Lexar, your fully intelligent assistant. How can I help you today?")
    automatic_backup_scheduler()
    ai_chat_mode()

def ai_chat_mode():
    print("\n=== Conversational AI (Smart Backup Management) ===")
    print("You can talk to me naturally, and I will always try to help.")
    print("(Type 'exit' to leave)")

    while True:
        user_input = input("Michael: ").lower()
        if "exit" in user_input:
            print("Goodbye, Michael. Have a great day!")
            save_memory(memory_data)
            break

        if user_input in memory_data["knowledge"]:
            print(memory_data["knowledge"][user_input])
            continue

        print("Let me think about that...")
        response = generate_intelligent_response(user_input)
        print(response)

        print("Would you like me to remember this answer? (yes/no)")
        choice = input("Michael: ").lower()
        if choice == "yes":
            memory_data["knowledge"][user_input] = response
            save_memory(memory_data)
            print("✅ I have learned this response.")

def generate_intelligent_response(query):
    try:
        response = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json").json()
        return response.get("AbstractText", "I couldn't find a clear answer, but I can help you understand it.")
    except:
        return "I couldn't connect to the web right now, but I can try to explain it myself."

def backup_memory():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"lexarv6_memory_backup_{timestamp}.json")
    shutil.copy(MEMORY_DB, backup_file)
    manage_backups()
    print(f"✅ Memory backed up at {backup_file}")

def restore_latest_backup():
    backups = sorted(os.listdir(BACKUP_DIR))
    if backups:
        latest_backup = os.path.join(BACKUP_DIR, backups[-1])
        try:
            with open(latest_backup, "r") as file:
                print("✅ Loaded the most recent backup.")
                return json.load(file)
        except:
            print("⚠️ Backup corrupted. Creating a new clean memory.")
            return {"commands": {}, "knowledge": pre_loaded_knowledge()}
    return {"commands": {}, "knowledge": pre_loaded_knowledge()}

def manage_backups():
    backups = sorted(os.listdir(BACKUP_DIR))
    if len(backups) > MAX_BACKUPS:
        for backup in backups[:-MAX_BACKUPS]:
            os.remove(os.path.join(BACKUP_DIR, backup))
        print("✅ Old backups cleaned up.")

def automatic_backup_scheduler():
    def backup_routine():
        while True:
            backup_memory()
            time.sleep(86400)  # Backup every 24 hours

    backup_thread = threading.Thread(target=backup_routine, daemon=True)
    backup_thread.start()

if __name__ == "__main__":
    greeting()
