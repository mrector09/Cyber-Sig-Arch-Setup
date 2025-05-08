
#!/bin/bash

echo -e "\e[32mStarting Cyber Sigilism Full Setup (Graphical Mode)...\e[0m"

# Function for Graphical Setup (Zenity)
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
    ) | zenity --progress --title="Cyber Sigilism Setup" --text="Setting up your system..." --width=400 --auto-close
}

# Hyprland and Configuration Setup
setup_hyprland() {
    mkdir -p ~/.config/hypr ~/.config/alacritty ~/.config/rofi ~/.config/swaylock ~/.config/conky ~/.config/neofetch ~/Pictures/Wallpapers

    # Hyprland Configuration
    cat <<EOF > ~/.config/hypr/hyprland.conf
monitor=,preferred,auto,0,0,1
col.active_border=#50fa7b
col.inactive_border=#282a36
col.background=#0a0a0e
col.text=#c5c8c6
rounding=8
exec-once=mpv --loop ~/Pictures/Wallpapers/cyber_dark_wallpaper.mp4 --wid=\$HYPRLAND_WID
exec-once=conky -c ~/.config/conky/cyber_conky.conf
bind=SUPER+ENTER,exec,alacritty
bind=SUPER+D,exec,rofi -show drun
bind=SUPER+SHIFT+L,exec,swaylock -f -c 0a0a0e
bind=SUPER+H,exec,~/.config/hypr/hotkey_menu.sh
bind=SUPER+X,exec,hyprctl dispatch closewindow
EOF

    # Create Hotkey Menu Script
    cat <<EOF > ~/.config/hypr/hotkey_menu.sh
#!/bin/bash
zenity --list --title="Cyber Sigilism Hotkeys" --width=500 --height=400 \
--column="Hotkey" --column="Function" \
"SUPER + ENTER" "Open Terminal (Alacritty)" \
"SUPER + D" "Open Rofi Launcher" \
"SUPER + SHIFT + L" "Lock Screen (Swaylock)" \
"SUPER + H" "Show Hotkey List" \
"SUPER + W" "Launch Firefox" \
"SUPER + T" "Launch Thunar File Manager" \
"SUPER + S" "Launch SimpleScreenRecorder" \
"SUPER + M" "Launch Metasploit (Terminal)" \
"SUPER + X" "Close Window Under Cursor"
EOF
    chmod +x ~/.config/hypr/hotkey_menu.sh
}

# Finalize Setup
finalize_setup() {
    chmod +x ~/.config/hypr/hotkey_menu.sh

    # Custom Rune NeoFetch
    cat <<EOF > ~/.config/neofetch/ascii.txt
            ██████╗ ██╗   ██╗███████╗██████╗ 
           ██╔═══██╗██║   ██║██╔════╝██╔══██╗
           ██║   ██║██║   ██║█████╗  ██████╔╝
           ██║   ██║██║   ██║██╔══╝  ██╔═══╝ 
           ╚██████╔╝╚██████╔╝███████╗██║     
            ╚═════╝  ╚═════╝ ╚══════╝╚═╝     
EOF

    # Set Neofetch Auto-Launch
    echo "neofetch --source ~/.config/neofetch/ascii.txt" >> ~/.zshrc

    # Completion Message
    zenity --info --text="Setup Complete! Reboot for changes to take effect." --width=400
}

# Run the Setup with Progress
show_progress
