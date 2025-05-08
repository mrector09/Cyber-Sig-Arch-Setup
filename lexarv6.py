
import os
import subprocess

# Lexarv6 Logo for TUI (ASCII Style)
lexar_logo = '''
=================================================
 ██████╗ ██╗      █████╗ ██████╗  █████╗ ██████╗ 
██╔═══██╗██║     ██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║   ██║██║     ███████║██████╔╝███████║██║  ██║
██║   ██║██║     ██╔══██║██╔═══╝ ██╔══██║██║  ██║
╚██████╔╝███████╗██║  ██║██║     ██║  ██║██████╔╝
 ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═════╝ 
      LEXARV6 - THE ULTIMATE AI SYSTEM             
=================================================
'''

def setup_lexarv6_service():
    print("\n=== Setting Up Lexarv6 as a System Service ===")
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
    print("\n=== Setting Up Secure HTTPS (SSL) ===")
    os.system("sudo apt install certbot -y")
    domain = input("Enter your domain (e.g., example.com): ")
    os.system(f"sudo certbot certonly --standalone -d {domain}")
    print("✅ HTTPS (SSL) setup complete. Make sure to configure SSL in the service file.")

def view_web_logs():
    print("\n=== Viewing Lexarv6 Web Dashboard Logs ===")
    os.system("journalctl -u lexarv6.service -f")

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
    else:
        print("Invalid choice.")

def lexarv6_tui():
    while True:
        print(lexar_logo)
        print("=== Main Menu ===")
        print("1. Web Dashboard Control (Service + HTTPS)")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            web_dashboard_control()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    lexarv6_tui()
