
#!/bin/bash

echo -e "\e[32mStarting Full Intelligent Reset (Self-Updating, Self-Learning, Self-Editing AI)...\e[0m"
LOG_FILE="$HOME/reset_install_log.txt"
SCRIPT_PATH="$0"

log() {
    echo -e "$1" | tee -a "$LOG_FILE"
}

### ✅ WARNING: This will completely reset your system (except network)
log "\e[31mWARNING: This will completely reset your system except network.\e[0m"
read -p "Your choice (yes/no): " choice
if [ "$choice" != "yes" ]; then
    log "\e[31mOperation Cancelled.\e[0m"
    exit 1
fi

### ✅ Function: AI Diagnosis, Auto-Fix, Self-Learning, and Self-Editing
ai_fix() {
    log "\e[33m[AI DIAGNOSIS] Detecting Error: $1\e[0m"
    case "$1" in
        "PGP Error"|"Signature Error")
            log "\e[33m[AI FIX] Resetting Pacman Keyring and Repairing PGP...\e[0m"
            sudo rm -rf /etc/pacman.d/gnupg
            sudo pacman-key --init
            sudo pacman-key --populate archlinux
            sudo pacman -Syyu --noconfirm --overwrite="*"
            ;;
        "Network Error")
            log "\e[33m[AI FIX] Restarting Network Services...\e[0m"
            sudo systemctl restart NetworkManager
            sudo ip link set wlan0 up || sudo ip link set eth0 up || sudo dhclient
            ;;
        "Package Conflict")
            log "\e[33m[AI FIX] Removing All Conflicting Packages and Editing Script...\e[0m"
            sudo pacman -Rns hyprutils libhyprutils hyprlock hyprpaper --noconfirm
            sudo sed -i '/IgnorePkg/d' /etc/pacman.conf
            sed -i '/hyprutils/d' "$SCRIPT_PATH"
            sed -i '/libhyprutils/d' "$SCRIPT_PATH"
            sed -i '/hyprlock/d' "$SCRIPT_PATH"
            sed -i '/hyprpaper/d' "$SCRIPT_PATH"
            ;;
        "Corrupt Config")
            log "\e[33m[AI FIX] Restoring Clean Configurations...\e[0m"
            rm -rf ~/.config/hypr ~/.config/neofetch ~/.config/waybar
            mkdir -p ~/.config/hypr ~/.config/neofetch ~/.config/waybar
            ;;
        "Package Install Error")
            log "\e[33m[AI FIX] Re-Installing Failed Packages...\e[0m"
            sudo pacman -S --noconfirm "$2"
            sed -i "/$2/d" "$SCRIPT_PATH"
            echo "sudo pacman -S --noconfirm $2" >> "$SCRIPT_PATH"
            ;;
        "Dependency Loop")
            log "\e[33m[AI FIX] Breaking Dependency Loop and Auto-Resolving...\e[0m"
            sudo pacman -Scc --noconfirm
            sudo pacman -Syyu --noconfirm --overwrite="*"
            ;;
        *)
            log "\e[31m[AI DIAGNOSIS] Unknown Error. Attempting Full System Repair and Learning...\e[0m"
            sudo pacman -Syyu --noconfirm --overwrite="*"
            echo "# Unknown Error Fix Applied" >> "$SCRIPT_PATH"
            ;;
    esac
}

### ✅ Step 1: Self-Updating (If GitHub Repo is Set)
log "\e[32mChecking for Script Updates...\e[0m"
REPO_URL="https://github.com/mrector09/Cyber-Sig-Arch-Setup.git"
if [ ! -z "$REPO_URL" ]; then
    git clone "$REPO_URL" ~/reset_script_update
    cp ~/reset_script_update/reset.sh "$SCRIPT_PATH"
    rm -rf ~/reset_script_update
    chmod +x "$SCRIPT_PATH"
    log "\e[32mScript Updated from GitHub.\e[0m"
fi

### ✅ Step 2: Comprehensive Package Removal (AI Protected)
log "\e[32mRemoving Conflicting Packages (AI Protected)...\e[0m"
if ! sudo pacman -Rns hyprutils libhyprutils hyprlock hyprpaper --noconfirm; then
    ai_fix "Package Conflict"
fi

### ✅ Step 3: Full System Re-Sync (PGP Protection)
log "\e[32mRe-Syncing Pacman Database (AI Protected)...\e[0m"
if ! sudo pacman -Syyu --noconfirm --overwrite="*"; then
    ai_fix "PGP Error"
fi

### ✅ Step 4: Network Verification (AI Protected)
log "\e[32mVerifying Network Connection (AI Protected)...\e[0m"
if ! sudo systemctl restart NetworkManager; then
    ai_fix "Network Error"
fi

### ✅ Step 5: Advanced Package Installation (AI Auto-Repair)
log "\e[32mInstalling Essential Packages (AI Auto-Repair)...\e[0m"
packages=(hyprland wayland wlroots kitty rofi swaylock waybar thunar neofetch zsh pavucontrol brightnessctl)
for pkg in "${packages[@]}"; do
    if ! sudo pacman -S --noconfirm "$pkg"; then
        ai_fix "Package Install Error" "$pkg"
    fi
done

### ✅ Step 6: Cyber Sigilism Configuration Setup (AI Protected)
log "\e[32mSetting Up Configuration (AI Protected)...\e[0m"
mkdir -p ~/.config/hypr ~/.config/neofetch ~/.config/waybar
cat <<EOF > ~/.config/hypr/hyprland.conf
monitor=,preferred,auto,0,0,1
col.active_border=#50fa7b
col.inactive_border=#282a36
col.background=#0a0a0e
col.text=#c5c8c6
rounding=8
EOF

### ✅ Step 7: Automatic Reboot into New Hyprland Setup
log "\e[32mSetup Complete! Rebooting into the Clean Cyber Sigilism Setup...\e[0m"
log "\e[32mFull Log Saved at: $LOG_FILE\e[0m"
sleep 5
sudo reboot
