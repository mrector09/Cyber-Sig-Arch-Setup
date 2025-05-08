
#!/bin/bash

echo -e "\e[32mStarting Cyber Sigilism Setup Restore...\e[0m"

# Step 1: Clean Up Any Corrupted Configurations
echo -e "\e[32mCleaning up any corrupted configuration files...\e[0m"
rm -rf ~/.config/hypr ~/.config/alacritty ~/.config/rofi ~/.config/swaylock ~/.config/conky ~/.config/neofetch ~/Pictures/Wallpapers

# Step 2: Create Fresh Configuration Directories
mkdir -p ~/.config/hypr ~/.config/alacritty ~/.config/rofi ~/.config/swaylock ~/.config/conky ~/.config/neofetch ~/Pictures/Wallpapers

# Step 3: Minimal Clean Hyprland Configuration
cat <<EOF > ~/.config/hypr/hyprland.conf
monitor=,preferred,auto,0,0,1
col.active_border=#50fa7b
col.inactive_border=#282a36
col.background=#0a0a0e
col.text=#c5c8c6
rounding=8

# Hotkeys
bind=SUPER+ENTER,exec,kitty  # Terminal
bind=SUPER+D,exec,rofi -show drun  # Application Launcher
bind=SUPER+SHIFT+L,exec,swaylock -f -c 0a0a0e  # Lock Screen
bind=SUPER+H,exec,~/.config/hypr/hotkey_menu.sh  # Hotkey List
bind=SUPER+X,exec,hyprctl dispatch closewindow  # Close Window Under Cursor
EOF

# Step 4: Create Clean Hotkey Menu
cat <<EOF > ~/.config/hypr/hotkey_menu.sh
#!/bin/bash
zenity --list --title="Cyber Sigilism Hotkeys" --width=500 --height=400 \
--column="Hotkey" --column="Function" \
"SUPER + ENTER" "Open Terminal (Kitty)" \
"SUPER + D" "Open Rofi Launcher" \
"SUPER + SHIFT + L" "Lock Screen (Swaylock)" \
"SUPER + H" "Show Hotkey List" \
"SUPER + X" "Close Window Under Cursor" \
"SUPER + W" "Launch Firefox" \
"SUPER + T" "Launch Thunar File Manager" \
"SUPER + S" "Launch SimpleScreenRecorder" \
"SUPER + M" "Launch Metasploit (Terminal)"
EOF
chmod +x ~/.config/hypr/hotkey_menu.sh

# Step 5: Neon Green Terminal (Kitty)
mkdir -p ~/.config/kitty
cat <<EOF > ~/.config/kitty/kitty.conf
background #0a0a0e
foreground #50fa7b
font_family JetBrainsMono Nerd Font
font_size 14
EOF

# Step 6: Custom Rune Neofetch
cat <<EOF > ~/.config/neofetch/ascii.txt
            ██████╗ ██╗   ██╗███████╗██████╗ 
           ██╔═══██╗██║   ██║██╔════╝██╔══██╗
           ██║   ██║██║   ██║█████╗  ██████╔╝
           ██║   ██║██║   ██║██╔══╝  ██╔═══╝ 
           ╚██████╔╝╚██████╔╝███████╗██║     
            ╚═════╝  ╚═════╝ ╚══════╝╚═╝     
EOF

# Auto-run Neofetch with Rune on Terminal Launch
echo "neofetch --source ~/.config/neofetch/ascii.txt" >> ~/.zshrc

# Step 7: Clean Swaylock (Lock Screen)
cat <<EOF > ~/.config/swaylock/config
colors {
    background: #0a0a0e
    ring: #50fa7b
    line: #282a36
    inside: #0a0a0e
    text: #c5c8c6
}
EOF

# Step 8: Restart Hyprland
echo -e "\e[32mReloading Hyprland...\e[0m"
hyprctl reload

echo -e "\e[32mCyber Sigilism Setup Restored Successfully!\e[0m"
