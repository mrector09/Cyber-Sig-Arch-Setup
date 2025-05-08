
import os
import subprocess
import time

# Lexarv5 Logo for TUI (ASCII Style)
lexar_logo = '''
=================================================
 ██████╗ ██╗      █████╗ ██████╗  █████╗ ██████╗ 
██╔═══██╗██║     ██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║   ██║██║     ███████║██████╔╝███████║██║  ██║
██║   ██║██║     ██╔══██║██╔═══╝ ██╔══██║██║  ██║
╚██████╔╝███████╗██║  ██║██║     ██║  ██║██████╔╝
 ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═════╝ 
      LEXARV5 - THE ULTIMATE AI SYSTEM             
=================================================
'''

def custom_os_setup():
    print(lexar_logo)
    print("=== Lexarv5 - Custom OS Setup Wizard ===")

    # Step 1: Desktop Environment Selection
    print("\nChoose Your Desktop Environment:")
    print("1. Hyprland (Default)")
    print("2. KDE Plasma")
    print("3. GNOME")
    choice = input("Choose an option: ")
    if choice == "2":
        desktop_env = "plasma-desktop"
    elif choice == "3":
        desktop_env = "gnome"
    else:
        desktop_env = "hyprland"

    # Step 2: Theme Selection
    print("\nChoose Your Theme Style:")
    print("1. Dark Theme (Default)")
    print("2. Light Theme")
    print("3. Custom Theme")
    theme_choice = input("Choose an option: ")
    if theme_choice == "2":
        theme = "Light"
    elif theme_choice == "3":
        theme = input("Enter your custom theme name: ")
    else:
        theme = "Dark"

    # Step 3: Custom Widgets
    print("\nChoose Additional Widgets:")
    print("1. System Monitor (Waybar)")
    print("2. Custom Dock (Plank)")
    print("3. Notification System (Dunst)")
    widgets = input("Choose (separate by commas): ")
    selected_widgets = [w.strip() for w in widgets.split(",")]

    # Step 4: Security Configuration
    print("\nSetting Up Advanced Security...")
    os.system("sudo pacman -S ufw openssh --noconfirm")
    os.system("sudo systemctl enable ufw")
    os.system("sudo ufw enable")
    os.system("sudo ufw default deny incoming")
    os.system("sudo ufw default allow outgoing")

    # Step 5: Secure VPN and Proxy Hopping (Optional)
    print("\nSecure Connection Options:")
    print("1. Secure VPN (OpenVPN)")
    print("2. Proxy Hopping (Socks5)")
    print("3. Both")
    security_choice = input("Choose an option: ")
    if security_choice == "1" or security_choice == "3":
        os.system("sudo pacman -S openvpn --noconfirm")
        print("Secure VPN installed.")
    if security_choice == "2" or security_choice == "3":
        os.system("sudo pacman -S proxychains-ng --noconfirm")
        print("Proxy Hopping installed.")

    # Step 6: Installing Desktop Environment
    print("\nInstalling Desktop Environment: " + desktop_env)
    os.system(f"sudo pacman -S {desktop_env} --noconfirm")

    # Step 7: Applying Theme and Widgets
    print("\nApplying Theme and Widgets...")
    if theme == "Dark":
        os.system("echo 'gtk-application-prefer-dark-theme=1' > ~/.config/gtk-3.0/settings.ini")
    for widget in selected_widgets:
        if widget.lower() == "system monitor":
            os.system("sudo pacman -S waybar --noconfirm")
        elif widget.lower() == "custom dock":
            os.system("sudo pacman -S plank --noconfirm")
        elif widget.lower() == "notification system":
            os.system("sudo pacman -S dunst --noconfirm")

    # Step 8: System Optimization
    print("\nOptimizing System Performance...")
    os.system("sudo sysctl -w vm.swappiness=10")
    os.system("sudo systemctl restart systemd-journald")

    # Step 9: Enabling Graphical Login (Automatic)
    print("\nEnabling Graphical Login with " + desktop_env)
    os.system("sudo systemctl set-default graphical.target")

    print("\n✅ Custom OS Setup Complete! Reboot to apply changes.")
    print("Use Lexarv5 for full control and customization.")

def lexarv5_tui():
    print(lexar_logo)
    print("1. Build Custom OS (Complete Setup with Configuration Wizard)")
    print("2. System Optimization")
    print("3. Secure VPN")
    print("4. Proxy Hopping")
    print("5. Intrusion Detection")
    print("0. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        custom_os_setup()
    elif choice == "2":
        optimize_system()
    elif choice == "3":
        start_vpn()
    elif choice == "4":
        proxy_hopping()
    elif choice == "5":
        intrusion_detection()
    elif choice == "0":
        print("Goodbye.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    print(lexar_logo)
    lexarv5_tui()
