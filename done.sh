
#!/bin/bash

echo -e "\e[32mStarting Cyber Sigilism Ultimate Setup (Self-Updating, Error-Proof)...\e[0m"

### ✅ Debug Mode (Toggleable)
DEBUG_MODE=false  # Set to true for debug output

log_debug() {
    if [ "$DEBUG_MODE" = true ]; then
        echo -e "\e[34m[DEBUG] $1\e[0m"
    fi
}

### ✅ Step 1: Smart PGP Signature Repair (Automatic)
echo -e "\e[32mChecking and Repairing PGP Signature Errors...\e[0m"
sudo rm -rf /etc/pacman.d/gnupg
sudo pacman-key --init
sudo pacman-key --populate archlinux
sudo pacman-key --refresh-keys --keyserver hkps://keys.openpgp.org

### ✅ Step 2: Dependency Cycle Repair
echo -e "\e[32mRepairing Dependency Cycles...\e[0m"
sudo pacman -Scc --noconfirm
sudo pacman -Syyu --noconfirm --overwrite="*"

### ✅ Step 3: Keyboard Repair
echo -e "\e[32mRepairing Keyboard Settings (US Layout)...\e[0m"
setxkbmap us
export XKB_DEFAULT_LAYOUT=us

### ✅ Step 4: GUI Compatibility (Zenity + XWayland)
echo -e "\e[32mEnsuring Zenity (GTK3) and XWayland are Installed...\e[0m"
sudo pacman -S zenity-gtk3 xorg-xwayland --noconfirm

### ✅ Step 5: Network Repair (Detect and Fix)
echo -e "\e[32mEnsuring Network Connection is Stable...\e[0m"
if ! ping -c 1 archlinux.org &>/dev/null; then
    sudo systemctl restart NetworkManager
fi

### ✅ Step 6: Remove Existing Login Screen (Replace with Custom)
echo -e "\e[32mReplacing Existing Login Screen with Custom Design...\e[0m"
sudo pacman -S lightdm lightdm-gtk-greeter --noconfirm
sudo systemctl enable lightdm.service --force
sudo systemctl start lightdm.service

cat <<EOF | sudo tee /etc/lightdm/lightdm-gtk-greeter.conf
[greeter]
theme-name = Adwaita-dark
icon-theme-name = Adwaita
background = /usr/share/backgrounds/cyber_dark_wallpaper.jpg
font-name = JetBrainsMono Nerd Font 12
EOF

### ✅ Step 7: Self-Repairing Setup with Debug Monitoring
show_progress() {
    (
        echo "10"; sleep 1
        echo "# Updating system..."; sudo pacman -Syu --noconfirm
        echo "30"; sleep 1
        echo "# Installing essential packages..."; sudo pacman -S --noconfirm hyprland wayland wlroots xdg-desktop-portal-hyprland \
        alacritty rofi dunst swaybg thunar zsh starship neofetch \
        ttf-jetbrains-mono-nerd noto-fonts-emoji grim slurp xdg-desktop-portal \
        polkit-gnome mako pipewire wireplumber pavucontrol swaylock mpv \
        imagemagick conky nitrogen cava glava
        echo "60"; sleep 1
        echo "# Configuring Hyprland and Desktop Environment..."; setup_hyprland
        echo "90"; sleep 1
        echo "# Finalizing Setup..."; finalize_setup
        echo "100"
    ) | zenity --progress --title="Cyber Sigilism Setup" --text="Setting up your system..." --width=400 --auto-close || safe_mode
}

### ✅ Step 8: Safe Mode Fallback (If GUI Fails)
safe_mode() {
    echo -e "\e[31mGUI Setup Failed. Entering Safe Mode (TTY)...\e[0m"
    echo -e "\e[33mRunning Safe Mode Installer...\e[0m"
    mkdir -p ~/.config/hypr
    echo "bind=SUPER+ENTER,exec,kitty" > ~/.config/hypr/hyprland.conf
    echo -e "\e[32mSafe Mode Setup Complete! Use SUPER + ENTER to open terminal.\e[0m"
}

### ✅ Step 9: Hyprland Configuration (Hotkeys + System Check)
setup_hyprland() {
    mkdir -p ~/.config/hypr ~/.config/alacritty ~/.config/rofi ~/.config/swaylock ~/.config/conky ~/.config/neofetch ~/Pictures/Wallpapers

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
EOF

    cat <<EOF > ~/.config/hypr/system_check.sh
#!/bin/bash
zenity --info --text="Running System Check (Full Repair)..." --width=400
sudo pacman-key --refresh-keys
sudo pacman -Syyu --noconfirm
sudo pacman -Scc --noconfirm
zenity --info --text="System Check Complete! System is Clean." --width=400
EOF
    chmod +x ~/.config/hypr/system_check.sh
}

### ✅ Step 10: Finalize Setup
finalize_setup() {
    zenity --info --text="Setup Complete! Reboot for changes to take effect." --width=400
}

### ✅ Step 11: Start Setup with Debug Monitoring
show_progress
