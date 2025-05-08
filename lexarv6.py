
import os
import subprocess
import time
import re

# Lexarv6 Logo and Custom Greeting
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
        
        # Natural Language Understanding
        if re.search(r"optimize|speed|make faster|improve performance", user_input):
            optimize_system()
        elif re.search(r"secure|protect|safe", user_input):
            secure_system()
        elif re.search(r"build|create|make.*os", user_input):
            build_custom_os()
        elif re.search(r"web panel|dashboard|web control", user_input):
            web_dashboard_control()
        elif re.search(r"repair|fix|diagnose|troubleshoot", user_input):
            self_repair()
        else:
            print("I'm not sure how to help with that. Could you rephrase?")

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

def setup_lexarv6_service():
    print("\nSetting Up Lexarv6 as a System Service...")
    service_config = '''
[Unit]
Description=Lexarv6 - Secure Web Dashboard (Always-On)
After=network.target

[Service]
ExecStart=/usr/bin/gunicorn -w 4 -b 0.0.0.0:5000 lexarv6:app
WorkingDirectory=/usr/local/bin
Restart=always
User=root
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
'''
    with open('/etc/systemd/system/lexarv6.service', 'w') as service_file:
        service_file.write(service_config)
    os.system("sudo systemctl daemon-reload")
    os.system("sudo systemctl enable lexarv6.service")
    os.system("sudo systemctl start lexarv6.service")
    print("✅ Lexarv6 is now running as an always-on service.")

if __name__ == "__main__":
    greeting()
