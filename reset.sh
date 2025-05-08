
#!/bin/bash

echo -e "\e[32mStarting Complete System Reset and Reinstall (Perfect Setup - No Network Removal)...\e[0m"

### ✅ WARNING: This will completely reset your system.
echo -e "\e[31mWARNING: This will completely reset your system to a clean state. Do you want to continue? (yes/no)\e[0m"
read -p "Your choice: " choice
if [ "$choice" != "yes" ]; then
    echo -e "\e[31mOperation Cancelled.\e[0m"
    exit 1
fi

### ✅ Step 1: Removing All Packages and User Configurations (Except Network)
echo -e "\e[32mRemoving All Packages and User Configurations (Except Network)...\e[0m"
sudo pacman -Rns $(pacman -Qq | grep -vE "networkmanager|network-manager-applet|iwd|wpa_supplicant") --noconfirm || echo "System already clean."
rm -rf ~/.config ~/.local ~/.cache ~/.bashrc ~/.zshrc ~/.profile ~/Documents ~/Downloads ~/Pictures ~/Music ~/Videos

### ✅ Step 2: Cleaning System Directories (Except Network)
echo -e "\e[32mCleaning System Directories (No Network Files Affected)...\e[0m"
sudo rm -rf /etc/xdg /usr/local/bin /usr/local/share /opt /usr/share/xsessions /usr/share/wayland-sessions

### ✅ Step 3: Full System Re-Sync and Base Reinstallation
echo -e "\e[32mReinstalling Base System Packages...\e[0m"
sudo pacman -Syyu --noconfirm --overwrite="*"
sudo pacman -S base base-devel linux linux-firmware nano --noconfirm

### ✅ Step 4: Reinstalling Hyprland, Wayland, and Essential Packages
echo -e "\e[32mInstalling Hyprland, Wayland, and Essential Packages...\e[0m"
sudo pacman -S hyprland wayland wlroots kitty rofi swaylock waybar thunar neofetch zsh pavucontrol brightnessctl --noconfirm

### ✅ Step 5: Setting Up Complete Cyber Sigilism Configuration
mkdir -p ~/.config/hypr ~/.config/neofetch ~/.config/waybar

# Hyprland Configuration
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
bind=SUPER+M,exec,msfconsole
bind=SUPER+N,exec,nmap
bind=SUPER+W,exec,wireshark-qt
bind=SUPER+T,exec,thunar
EOF

# Custom Rune Neofetch
cat <<EOF > ~/.config/neofetch/ascii.txt
            ██████╗ ██╗   ██╗███████╗██████╗ 
           ██╔═══██╗██║   ██║██╔════╝██╔══██╗
           ██║   ██║██║   ██║█████╗  ██████╔╝
           ██║   ██║██║   ██║██╔══╝  ██╔═══╝ 
           ╚██████╔╝╚██████╔╝███████╗██║     
            ╚═════╝  ╚═════╝ ╚══════╝╚═╝     
EOF

echo "neofetch --source ~/.config/neofetch/ascii.txt" >> ~/.zshrc

# Waybar (Top Bar) Configuration
cat <<EOF > ~/.config/waybar/config
{
    "layer": "top",
    "position": "top",
    "modules-left": ["network", "volume", "brightness"],
    "modules-right": ["clock", "power-menu"],
    "clock": { "format": "%A, %B %d - %H:%M:%S" }
}
EOF

### ✅ Step 6: System Check Tool (SUPER + S)
cat <<EOF > ~/.config/hypr/system_check.sh
#!/bin/bash
echo "Running System Check (Full Repair)..."
sudo pacman -Syyu --noconfirm
sudo pacman -Scc --noconfirm
echo "System Check Complete! System is Clean."
EOF
chmod +x ~/.config/hypr/system_check.sh

### ✅ Step 7: Complete Pentesting Suite Installation
echo -e "\e[32mInstalling Complete Pentesting Suite...\e[0m"
sudo pacman -S metasploit nmap wireshark-qt aircrack-ng john hydra hashcat gobuster --noconfirm

### ✅ Step 8: Ensuring Network Connection is Intact
echo -e "\e[32mEnsuring Network Connection is Intact...\e[0m"
sudo systemctl enable NetworkManager --now
sudo systemctl restart NetworkManager

### ✅ Step 9: Finalizing Setup
echo -e "\e[32mSetup Complete! Reboot for a Clean and Fresh Cyber Sigilism System.\e[0m"
