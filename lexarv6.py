
import os
import subprocess
import time

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
    print("Welcome, Michael! How can I assist you today?")

# Self-Repair System (Automatic Error Detection and Fix)
def self_repair():
    print("\n=== Lexarv6 - Self-Repair System ===")
    # Detect and fix service errors
    service_status = subprocess.getoutput("systemctl is-active lexarv6.service")
    if "inactive" in service_status or "failed" in service_status:
        print("⚠️ Lexarv6 Service is Down. Repairing...")
        os.system("sudo systemctl restart lexarv6.service")
        print("✅ Lexarv6 Service Restarted Successfully.")

    # Detect and fix Gunicorn/Flask Errors
    try:
        import gunicorn
        import flask
        print("✅ Gunicorn and Flask are correctly installed.")
    except ImportError:
        print("⚠️ Gunicorn or Flask Missing. Installing...")
        os.system("pip install gunicorn flask")

    # Auto-repair Configuration Errors (Hyprland, Web)
    if not os.path.exists("/usr/local/bin/lexarv6.py"):
        print("⚠️ Lexarv6 File Missing. Repairing...")
        os.system("curl -o /usr/local/bin/lexarv6.py https://YOUR_GITHUB_REPO_URL/lexarv6.py")
        os.system("chmod +x /usr/local/bin/lexarv6.py")
        print("✅ Lexarv6 Restored Successfully.")

def web_dashboard_control():
    print("\n=== Web Dashboard Control ===")
    print("1. Enable Lexarv6 as a System Service")
    print("2. Start/Stop Web Dashboard")
    print("3. Set Up Secure HTTPS (SSL)")
    print("4. View Web Dashboard Logs")
    choice = input("Choose an option: ")

    if choice == "1":
        setup_lexarv6_service()
    elif choice == "2":
        print("1. Start Service\n2. Stop Service")
        action = input("Choose an option: ")
        if action == "1":
            os.system("sudo systemctl start lexarv6.service")
            print("✅ Lexarv6 Web Dashboard Started.")
        elif action == "2":
            os.system("sudo systemctl stop lexarv6.service")
            print("✅ Lexarv6 Web Dashboard Stopped.")
    elif choice == "3":
        setup_https()
    elif choice == "4":
        view_web_logs()

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

def setup_https():
    print("\nSetting Up Secure HTTPS (SSL)")
    os.system("sudo apt install certbot -y")
    domain = input("Enter your domain (e.g., example.com): ")
    os.system(f"sudo certbot certonly --standalone -d {domain}")
    print("✅ HTTPS (SSL) setup complete. Make sure to configure SSL in the service file.")

def lexarv6_tui():
    self_repair()
    greeting()
    while True:
        print("\n=== Main Menu ===")
        print("1. Web Dashboard Control (Service + HTTPS)")
        print("2. Self-Repair System (Automatic)")
        print("3. Advanced Tools")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            web_dashboard_control()
        elif choice == "2":
            self_repair()
        elif choice == "3":
            print("Advanced Tools Coming Soon...")
        elif choice == "0":
            print("Goodbye, Michael.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    lexarv6_tui()
