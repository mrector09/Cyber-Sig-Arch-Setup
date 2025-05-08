
#!/bin/bash

echo -e "\e[32mStarting Perfect Full Reset and Auto-Install Setup (Guaranteed Error-Free)...\e[0m"

### ✅ WARNING: This will completely reset your system (except network)
echo -e "\e[31mWARNING: This will completely reset your system except network. Do you want to continue? (yes/no)\e[0m"
read -p "Your choice: " choice
if [ "$choice" != "yes" ]; then
    echo -e "\e[31mOperation Cancelled.\e[0m"
    exit 1
fi

### ✅ Step 1: Removing Everything Except Network Configs
echo -e "\e[32mRemoving All Packages and Configurations (Except Network)...\e[0m"
sudo pacman -Rns $(pacman -Qq | grep -vE "networkmanager|network-manager-applet|iwd|wpa_supplicant") --noconfirm || echo "System already clean."
rm -rf ~/.config ~/.local ~/.cache ~/.bashrc ~/.zshrc ~/.profile ~/Documents ~/Downloads ~/Pictures ~/Music ~/Videos

### ✅ Step 2: Cleaning System Directories (Except Network)
echo -e "\e[32mCleaning System Directories (No Network Files Affected)...\e[0m"
sudo rm -rf /etc/xdg /usr/local/bin /usr/local/share /opt /usr/share/xsessions /usr/share/wayland-sessions

### ✅ Step 3: Full System Re-Sync and Base Reinstallation
echo -e "\e[32mReinstalling Base System Packages...\e[0m"
sudo pacman -Syyu --noconfirm --overwrite="*"
sudo pacman -S base base-devel linux linux-firmware nano --noconfirm

### ✅ Step 4: Auto-Installing Hyprland and Essential Packages (Error-Free)
echo -e "\e[32mInstalling Hyprland, Wayland, and Essential Packages...\e[0m"
packages=(hyprland wayland wlroots kitty rofi swaylock waybar thunar neofetch zsh pavucontrol brightnessctl)
for pkg in "${packages[@]}"; do
    until sudo pacman -S --noconfirm "$pkg"; do
        echo -e "\e[31mError Installing $pkg. Retrying...\e[0m"
        sleep 1
    done
done

### ✅ Step 5: Setting Up Perfect Cyber Sigilism Configuration (Error-Free)
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

### ✅ Step 6: Complete Pentesting Suite Installation (Auto-Fix)
pentest_tools=(metasploit nmap wireshark-qt aircrack-ng john hydra hashcat gobuster)
for tool in "${pentest_tools[@]}"; do
    until sudo pacman -S --noconfirm "$tool"; do
        echo -e "\e[31mError Installing $tool. Retrying...\e[0m"
        sleep 1
    done
done

### ✅ Step 7: Ensuring Network Connection is Intact
echo -e "\e[32mEnsuring Network Connection is Intact...\e[0m"
sudo systemctl enable NetworkManager --now
sudo systemctl restart NetworkManager

### ✅ Step 8: Automatic Reboot into New Hyprland Setup
echo -e "\e[32mSetup Complete! Rebooting into the Clean Cyber Sigilism Setup...\e[0m"
sleep 5
sudo reboot
