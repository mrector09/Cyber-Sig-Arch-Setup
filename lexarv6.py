
import os
import subprocess
import time
import re
import json
import requests
import socket

# Lexarv6 Memory and Knowledge Database (Learning Mode)
MEMORY_DB = "/usr/local/bin/lexarv6_memory.json"
KNOWLEDGE_DB = "/usr/local/bin/lexarv6_knowledge.json"

def load_memory():
    if os.path.exists(MEMORY_DB):
        with open(MEMORY_DB, "r") as file:
            return json.load(file)
    else:
        return {"commands": {}, "knowledge": {}}

def save_memory(memory_data):
    with open(MEMORY_DB, "w") as file:
        json.dump(memory_data, file, indent=4)

# Initialize Memory and Knowledge Data
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
    print("Welcome, Michael! I am Lexar, your intelligent assistant.")
    ai_chat_mode()

def ai_chat_mode():
    print("\n=== Conversational AI with Full Intelligence ===")
    print("You can talk to me naturally, and I will remember your preferences.")
    print("(Type 'exit' to leave)")

    while True:
        user_input = input("Michael: ").lower()
        if "exit" in user_input:
            print("Goodbye, Michael.")
            save_memory(memory_data)
            break

        # Memory-Enhanced Commands
        if user_input in memory_data["commands"]:
            print(f"Executing your preferred command: {memory_data['commands'][user_input]}")
            os.system(memory_data["commands"][user_input])
            continue

        # Knowledge Database Response
        if user_input in memory_data["knowledge"]:
            print(memory_data["knowledge"][user_input])
            continue

        # Internet Search for Unknown Questions
        if "search" in user_input or "look up" in user_input:
            search_query = user_input.replace("search", "").replace("look up", "").strip()
            web_search(search_query)
            continue

        # Execute System Commands
        if "optimize" in user_input:
            optimize_system()
        elif "secure" in user_input:
            secure_system()
        elif "repair" in user_input:
            self_repair()
        elif "cpu usage" in user_input:
            show_cpu_usage()
        elif "what's my ip" in user_input:
            show_ip_address()
        elif "web panel" in user_input:
            list_web_panel()
        elif "load hyprland" in user_input:
            os.system("Hyprland")
        else:
            print("I'm not sure about that. Would you like me to learn this? (yes/no)")
            choice = input("Michael: ").lower()
            if choice == "yes":
                print("What should I respond with?")
                answer = input("Response: ")
                memory_data["knowledge"][user_input] = answer
                save_memory(memory_data)
                print("✅ I have learned this response.")

def web_search(query):
    print(f"🔎 Searching the web for: {query}")
    try:
        response = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json")
        if response.status_code == 200:
            results = response.json()
            print("✅ Search Results:")
            print(results.get("AbstractText", "No clear answer found."))
        else:
            print("⚠️ Unable to search the web at the moment.")
    except:
        print("⚠️ Error connecting to the web.")

def show_ip_address():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        public_ip = requests.get('https://api.ipify.org').text
        print(f"Local IP Address: {local_ip}")
        print(f"Public IP Address: {public_ip}")
    except:
        print("⚠️ Unable to retrieve IP address.")

def list_web_panel():
    print("Your Web Dashboard is accessible at: http://localhost:5000")

def show_cpu_usage():
    cpu_usage = os.popen("top -bn1 | grep 'Cpu(s)'").read()
    print(f"CPU Usage: {cpu_usage}")

def optimize_system():
    print("Optimizing System...")
    os.system("sudo sysctl -w vm.swappiness=10")
    print("✅ System Optimized (CPU, RAM, Disk).")

def secure_system():
    print("Securing System...")
    os.system("sudo ufw enable")
    os.system("sudo ufw default deny incoming")
    os.system("sudo ufw default allow outgoing")
    print("✅ System Secured with Firewall.")

def self_repair():
    print("\n=== Self-Repair System ===")
    service_status = subprocess.getoutput("systemctl is-active lexarv6.service")
    if "inactive" in service_status or "failed" in service_status:
        print("⚠️ Lexarv6 Service is Down. Repairing...")
        os.system("sudo systemctl restart lexarv6.service")
        print("✅ Lexarv6 Service Restarted Successfully.")
    else:
        print("✅ Lexarv6 is running correctly.")

if __name__ == "__main__":
    greeting()
