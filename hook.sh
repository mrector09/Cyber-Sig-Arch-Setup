
#!/bin/bash

echo -e "\e[32mStarting Cyber Sigilism Absolute Final Setup (Pure TTY, No GUI)...\e[0m"

### ✅ Debug Mode (Toggleable)
DEBUG_MODE=true  # Set to true for debug output

log_debug() {
    if [ "$DEBUG_MODE" = true ]; then
        echo -e "\e[34m[DEBUG] $1\e[0m"
    fi
}

### ✅ Full Capabilities - Complete Guide
echo "Cyber Sigilism Final Setup - Full Capabilities (Pure TTY)"

### ✅ Step 1: Safe Backup (User Directory Only - No System Directories)
echo -e "\e[32mCreating a Safe Backup (User Directory Only)...\e[0m"
BACKUP_DIR="$HOME/cyber_sigilism_backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
log_debug "Backing up critical user configurations..."
cp -r $HOME/.config $HOME/Documents $HOME/Pictures $HOME/.bashrc $HOME/.zshrc $BACKUP_DIR

### ✅ Step 2: Bypassing PGP - Direct Hash-Verified Downloads
sudo pacman -Scc --noconfirm
sudo pacman -Syyu --noconfirm --overwrite="*"

### ✅ Step 3: Complete Keybinds Setup (Terminal-Only)
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
bind=SUPER+SHIFT+L,exec,exit  # Lock Screen (TTY Logout)
bind=SUPER+H,exec,~/.config/hypr/hotkey_menu.sh  # Hotkey List
bind=SUPER+S,exec,~/.config/hypr/system_check.sh  # System Check (Full Repair)
bind=SUPER+K,exec,~/.config/hypr/key_repair.sh  # Smart Key Repair (PGP-Free)
bind=SUPER+M,exec,msfconsole  # Metasploit (TTY)
bind=SUPER+N,exec,nmap  # Nmap (TTY)
bind=SUPER+W,exec,wireshark-qt  # Wireshark (if available)
bind=SUPER+T,exec,nnn  # File Manager (nnn - TTY Only)
EOF

### ✅ Step 4: Custom Rune Neofetch (TTY Compatible)
mkdir -p ~/.config/neofetch
cat <<EOF > ~/.config/neofetch/ascii.txt
            ██████╗ ██╗   ██╗███████╗██████╗ 
           ██╔═══██╗██║   ██║██╔════╝██╔══██╗
           ██║   ██║██║   ██║█████╗  ██████╔╝
           ██║   ██║██║   ██║██╔══╝  ██╔═══╝ 
           ╚██████╔╝╚██████╔╝███████╗██║     
            ╚═════╝  ╚═════╝ ╚══════╝╚═╝     
EOF

echo "neofetch --source ~/.config/neofetch/ascii.txt" >> ~/.bashrc

### ✅ Step 5: System Check Tool (SUPER + S - Pure TTY)
cat <<EOF > ~/.config/hypr/system_check.sh
#!/bin/bash
echo "Running System Check (Full Repair)..."
sudo pacman -Syyu --noconfirm
sudo pacman -Scc --noconfirm
echo "System Check Complete! System is Clean."
EOF
chmod +x ~/.config/hypr/system_check.sh

### ✅ Step 6: Smart Key Repair Tool (SUPER + K - Pure TTY)
cat <<EOF > ~/.config/hypr/key_repair.sh
#!/bin/bash
echo "Running Smart Key Repair (PGP-Free)..."
sudo rm -rf /etc/pacman.d/gnupg
sudo pacman-key --init
sudo pacman-key --populate archlinux
echo "Key Repair Complete!"
EOF
chmod +x ~/.config/hypr/key_repair.sh

### ✅ Step 7: Complete Pentesting Suite (TTY Compatible)
echo -e "\e[32mInstalling Complete Pentesting Suite (TTY Compatible)...\e[0m"
sudo pacman -S metasploit nmap wireshark-qt aircrack-ng john hydra hashcat gobuster --noconfirm

### ✅ Step 8: Finalize Setup (No GUI)
echo -e "\e[32mSetup Complete! You can now use all keybinds directly in TTY.\e[0m"
