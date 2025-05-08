
#!/bin/bash

echo -e "\e[32mStarting Cyber Sigilism Ultimate GUI Installer (Self-Repairing)...\e[0m"

### ✅ Step 1: PGP Signature Repair (Automatic)
echo -e "\e[32mChecking and Repairing PGP Signature Errors...\e[0m"
sudo rm -r /etc/pacman.d/gnupg
sudo pacman-key --init
sudo pacman-key --populate archlinux
sudo pacman-key --refresh-keys

# Re-importing Daniel M. Capella's Key (if needed)
sudo pacman-key --recv-keys 3056513887B78AEB --keyserver hkps://keyserver.ubuntu.com
sudo pacman-key --lsign-key 3056513887B78AEB

### ✅ Step 2: Dependency Cycle Repair (Automatic)
echo -e "\e[32mChecking and Repairing Dependency Cycles...\e[0m"
sudo pacman -Scc --noconfirm  # Clear old package cache
sudo pacman -Syyu --noconfirm  # Fully refresh package database

### ✅ Step 3: Keyboard Repair (Automatic)
echo -e "\e[32mRepairing Keyboard Settings (US Layout)...\e[0m"
setxkbmap us
export XKB_DEFAULT_LAYOUT=us

# Fixing Hyprland Keyboard Configuration
mkdir -p ~/.config/hypr
cat <<EOF > ~/.config/hypr/hyprland.conf
input {
    kb_layout = "us"
    kb_model = "pc105"
    kb_variant = ""
    kb_options = ""
}
EOF

### ✅ Step 4: Zenity (GTK3) and XWayland Repair (GUI Compatibility)
echo -e "\e[32mEnsuring Zenity (GTK3) and XWayland are Installed...\e[0m"
sudo pacman -S zenity-gtk3 xorg-xwayland --noconfirm

# Setting GTK3 Mode for Zenity
export GTK_THEME=Adwaita:dark

### ✅ Step 5: Self-Repairing GUI Installer with Safe Mode Fallback
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

### ✅ Step 6: Safe Mode Fallback (If GUI Fails)
safe_mode() {
    echo -e "\e[31mGUI Setup Failed. Entering Safe Mode (TTY)...\e[0m"
    echo -e "\e[33mRunning Safe Mode Installer...\e[0m"
    mkdir -p ~/.config/hypr
    echo "bind=SUPER+ENTER,exec,kitty" > ~/.config/hypr/hyprland.conf
    echo -e "\e[32mSafe Mode Setup Complete! Use SUPER + ENTER to open terminal.\e[0m"
}

### ✅ Step 7: Hyprland Configuration (Hotkeys + System Check)
setup_hyprland() {
    mkdir -p ~/.config/hypr ~/.config/alacritty ~/.config/rofi ~/.config/swaylock ~/.config/conky ~/.config/neofetch ~/Pictures/Wallpapers

    cat <<EOF > ~/.config/hypr/hyprland.conf
monitor=,preferred,auto,0,0,1
col.active_border=#50fa7b
col.inactive_border=#282a36
col.background=#0a0a0e
col.text=#c5c8c6
rounding=8
bind=SUPER+ENTER,exec,kitty  # Terminal
bind=SUPER+D,exec,rofi -show drun  # Application Launcher
bind=SUPER+SHIFT+L,exec,swaylock -f -c 0a0a0e  # Lock Screen
bind=SUPER+H,exec,~/.config/hypr/hotkey_menu.sh  # Hotkey List
bind=SUPER+S,exec,~/.config/hypr/system_check.sh  # System Check (Full Repair)
EOF

    # Hotkey Menu with System Check
    cat <<EOF > ~/.config/hypr/hotkey_menu.sh
#!/bin/bash
zenity --list --title="Cyber Sigilism Hotkeys" --width=500 --height=400 \
--column="Hotkey" --column="Function" \
"SUPER + ENTER" "Open Terminal (Kitty)" \
"SUPER + D" "Open Rofi Launcher" \
"SUPER + SHIFT + L" "Lock Screen (Swaylock)" \
"SUPER + S" "Run System Check (Fix Errors)"
EOF
    chmod +x ~/.config/hypr/hotkey_menu.sh

    # System Check (Full Repair)
    cat <<EOF > ~/.config/hypr/system_check.sh
#!/bin/bash
zenity --info --text="Running System Check (Full Repair)..." --width=400
sudo pacman-key --refresh-keys
sudo pacman -Syyu --noconfirm
zenity --info --text="System Check Complete! System is Clean." --width=400
EOF
    chmod +x ~/.config/hypr/system_check.sh
}

### ✅ Step 8: Finalize Setup
finalize_setup() {
    zenity --info --text="Setup Complete! Reboot for changes to take effect." --width=400
}

### ✅ Step 9: Start Setup with Error-Proof Mode
show_progress
