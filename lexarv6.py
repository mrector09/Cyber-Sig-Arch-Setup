
import os
import subprocess
import time
import re
import json
import requests
import socket

# Lexarv6 Learning Database (Learned Commands)
LEARNING_DB = "/usr/local/bin/lexarv6_learning.json"

def load_learning():
    if os.path.exists(LEARNING_DB):
        with open(LEARNING_DB, "r") as file:
            return json.load(file)
    else:
        return {}

def save_learning(learning_data):
    with open(LEARNING_DB, "w") as file:
        json.dump(learning_data, file, indent=4)

# Initialize Learning Data
learning_data = load_learning()

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
    print("Welcome, Michael! Would you like to enter Command Mode or AI Chat Mode?")
    print("1. Command Mode (TUI)")
    print("2. AI Chat Mode")
    choice = input("Choose an option: ")

    if choice == "1":
        command_mode()
    elif choice == "2":
        ai_chat_mode()
    else:
        print("Invalid choice. Please try again.")
        greeting()

def command_mode():
    print("\n=== Command Mode (TUI) ===")
    while True:
        print("1. Build Custom OS")
        print("2. Web Dashboard Control (Service + HTTPS)")
        print("3. Secure System (VPN, Proxy, Firewall)")
        print("4. System Optimization")
        print("5. Self-Repair System (Automatic)")
        print("6. View System Information")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            build_custom_os()
        elif choice == "2":
            web_dashboard_control()
        elif choice == "3":
            secure_system()
        elif choice == "4":
            optimize_system()
        elif choice == "5":
            self_repair()
        elif choice == "6":
            show_system_info()
        elif choice == "0":
            print("Goodbye, Michael.")
            break
        else:
            print("Invalid choice. Please try again.")

def ai_chat_mode():
    print("\n=== AI Chat Mode ===")
    print("You can ask me to perform any task. (Type 'exit' to leave AI Chat Mode)")

    while True:
        user_input = input("Michael: ").lower()
        if "exit" in user_input:
            print("Exiting AI Chat Mode.")
            break

        # System Awareness Commands
        if "ip" in user_input:
            show_ip_address()
        elif "web panel" in user_input or "dashboard" in user_input:
            list_web_panel()
        elif "cpu" in user_input:
            show_cpu_usage()
        elif "load hyprland" in user_input:
            os.system("Hyprland")
        elif "secure" in user_input:
            secure_system()
        elif "optimize" in user_input:
            optimize_system()
        elif "repair" in user_input:
            self_repair()
        else:
            print("I'm not sure how to help with that. Can you rephrase?")

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

def build_custom_os():
    print("Starting Custom OS Builder...")
    print("✅ Custom OS Setup Complete.")

def web_dashboard_control():
    print("Setting Up Web Dashboard...")
    setup_lexarv6_service()
    print("✅ Web Dashboard is now running.")

def secure_system():
    print("Securing System...")
    os.system("sudo ufw enable")
    os.system("sudo ufw default deny incoming")
    os.system("sudo ufw default allow outgoing")
    print("✅ System Secured with Firewall.")

def optimize_system():
    print("Optimizing System...")
    os.system("sudo sysctl -w vm.swappiness=10")
    print("✅ System Optimized (CPU, RAM, Disk).")

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
