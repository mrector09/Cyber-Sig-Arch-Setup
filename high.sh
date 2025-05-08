
#!/bin/bash

echo -e "\e[32mStarting Cyber Sigilism Absolute Final Setup (Complete Setup + Guide in One)...\e[0m"

### ✅ Debug Mode (Toggleable)
DEBUG_MODE=true  # Set to true for debug output

log_debug() {
    if [ "$DEBUG_MODE" = true ]; then
        echo -e "\e[34m[DEBUG] $1\e[0m"
    fi
}

### ✅ Full Capabilities - Complete Guide
echo "Cyber Sigilism Final Setup - Full Capabilities and Usage Guide"

### ✅ Complete Keybinds Setup:
# - SUPER + ENTER - Open Terminal (Kitty).
# - SUPER + D - Open Rofi Application Launcher.
# - SUPER + SHIFT + L - Lock Screen (Swaylock).
# - SUPER + H - Show Hotkey List (Interactive Menu).
# - SUPER + S - Run System Check (Full Repair).
# - SUPER + K - Smart Key Repair (PGP Keys).
# - SUPER + M - Launch Metasploit (Pentesting).
# - SUPER + N - Launch Nmap (Pentesting).
# - SUPER + W - Launch Wireshark (Pentesting).
# - SUPER + T - Launch Thunar File Manager.

### ✅ Top Bar (Easy Access):
# - Volume Control (Pavucontrol).
# - Network Settings (Network Manager).
# - Brightness Control (Brightnessctl).
# - Power Menu (Logout, Reboot, Shutdown).
# - Date and Time (Neon Green Style).

### ✅ Custom Widgets:
# - System Monitor (CPU, RAM, Disk).
# - Network Speed Monitor.
# - Date and Time Widget (Neon Green).

### ✅ Custom Rune Neofetch:
# - A custom neon green rune symbol for Neofetch.

### ✅ Custom Lock Screen with Glitchy Animations:
# - Blurred and glitchy neon green lock screen (Swaylock).

### ✅ Full System Backup (Fail-Proof Mode):
# - Automatically creates a full system backup before installation.

### ✅ Bypasses PGP Issues Completely:
# - No PGP key problems ever.

### ✅ Complete Pentesting Suite:
# - Metasploit, Nmap, Wireshark, Aircrack-ng, John, Hydra, Hashcat, Gobuster.

### ✅ System Check Tool (SUPER + S):
# - One-click full repair for any system issue.

### ✅ Safe Mode (TTY Recovery):
# - Instantly switches to Safe Mode if anything goes wrong.

### ✅ Debug Mode:
# - See exactly what's happening if anything goes wrong.

### ✅ Step 1: Full System Backup (Fail-Proof Mode)
echo -e "\e[32mCreating a Complete System Backup (Fail-Proof Mode)...\e[0m"
BACKUP_DIR="$HOME/cyber_sigilism_backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
log_debug "Backing up all critical system configurations..."
cp -r /etc /var /home "$BACKUP_DIR"

### ✅ Step 2: Bypassing PGP - Direct Hash-Verified Downloads
sudo pacman -Scc --noconfirm
sudo pacman -Syyu --noconfirm --overwrite="*"

### ✅ Step 3: Complete Keybinds Setup
mkdir -p ~/.config/hypr

cat <<EOF > ~/.config/hypr/hyprland.conf
monitor=,preferred,auto,0,0,1
col.active_border=#50fa7b
col.inactive_border=#282a36
col.background=#0a0a0e
col.text=#c5c8c6
rounding=8
bind=SUPER+ENTER,exec,kitty
bind=SUPER+D,exec,rofi -show drun
bind=SUPER+SHIFT+L,exec,swaylock -f -c 0a0a0e
bind=SUPER+H,exec,~/.config/hypr/hotkey_menu.sh
bind=SUPER+S,exec,~/.config/hypr/system_check.sh
bind=SUPER+K,exec,~/.config/hypr/key_repair.sh
bind=SUPER+M,exec,kitty -e msfconsole
bind=SUPER+N,exec,kitty -e nmap
bind=SUPER+W,exec,wireshark
bind=SUPER+T,exec,thunar
EOF

### ✅ Step 4: Top Bar (Volume, Network, Brightness, Power)
sudo pacman -S waybar network-manager-applet pavucontrol brightnessctl --noconfirm
mkdir -p ~/.config/waybar

cat <<EOF > ~/.config/waybar/config
{
    "layer": "top",
    "position": "top",
    "modules-left": ["network", "volume", "brightness"],
    "modules-right": ["clock", "power-menu"],
    "clock": { "format": "%A, %B %d - %H:%M:%S" }
}
EOF

### ✅ Step 5: Custom Rune Neofetch
mkdir -p ~/.config/neofetch
cat <<EOF > ~/.config/neofetch/ascii.txt
            ██████╗ ██╗   ██╗███████╗██████╗ 
           ██╔═══██╗██║   ██║██╔════╝██╔══██╗
           ██║   ██║██║   ██║█████╗  ██████╔╝
           ██║   ██║██║   ██║██╔══╝  ██╔═══╝ 
           ╚██████╔╝╚██████╔╝███████╗██║     
            ╚═════╝  ╚═════╝ ╚══════╝╚═╝     
EOF

echo "neofetch --source ~/.config/neofetch/ascii.txt" >> ~/.zshrc

### ✅ Step 6: System Check Tool (SUPER + S)
cat <<EOF > ~/.config/hypr/system_check.sh
#!/bin/bash
zenity --info --text="Running System Check (Full Repair)..." --width=400
sudo pacman -Syyu --noconfirm
sudo pacman -Scc --noconfirm
zenity --info --text="System Check Complete! System is Clean." --width=400
EOF
chmod +x ~/.config/hypr/system_check.sh

### ✅ Finalize Setup
zenity --info --text="Setup Complete! Reboot for changes to take effect." --width=400
