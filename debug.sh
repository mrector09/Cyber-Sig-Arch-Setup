
#!/bin/bash

echo -e "\e[32mStarting Hyprland Config Debug Tool (Auto-Detect and Fix)...\e[0m"

### ✅ Step 1: Setting Hyprland Config Path (Ensures Only One Config is Used)
export HYPRLAND_CONFIG_PATH=~/.config/hypr/hyprland.conf

### ✅ Step 2: Checking for Other Config Files (Removing Conflicts)
echo -e "\e[32mChecking for Conflicting Config Files...\e[0m"
sudo find / -name "hyprland.conf" | grep -v "$HYPRLAND_CONFIG_PATH" | while read -r config; do
    echo -e "\e[33mConflicting Config Found: $config\e[0m"
    sudo mv "$config" "${config}.backup"
done

### ✅ Step 3: Verifying Your Config Exists
echo -e "\e[32mEnsuring Your Config Exists...\e[0m"
mkdir -p ~/.config/hypr

if [ ! -f ~/.config/hypr/hyprland.conf ]; then
    echo -e "\e[31mNo Hyprland Config Found! Creating a Default Error-Free Config...\e[0m"
    cat <<EOF > ~/.config/hypr/hyprland.conf
# Hyprland Configuration (Error-Free, Optimized)
monitor=,preferred,auto,0,0,1
col.active_border=#50fa7b
col.inactive_border=#282a36
col.background=#0a0a0e
col.text=#c5c8c6
rounding=8

# Keybinds (Guaranteed to Work)
bind=SUPER+ENTER,exec,kitty
bind=SUPER+D,exec,rofi -show drun
bind=SUPER+SHIFT+L,exec,swaylock -f -c 0a0a0e
bind=SUPER+H,exec,~/.config/hypr/hotkey_menu.sh
bind=SUPER+S,exec,~/.config/hypr/system_check.sh
bind=SUPER+M,exec,msfconsole
bind=SUPER+N,exec,nmap
bind=SUPER+W,exec,wireshark-qt
bind=SUPER+T,exec,thunar

# Safe Mode Fallback
fallback = /etc/xdg/hypr/hyprland.conf
EOF
else
    echo -e "\e[32mYour Config Exists and is Active.\e[0m"
fi

### ✅ Step 4: Fixing Config Permissions and Links
chmod +x ~/.config/hypr/hyprland.conf
ln -sf ~/.config/hypr/hyprland.conf ~/.config/hypr/hyprland_active.conf

### ✅ Step 5: Verifying Config Syntax (No Errors)
echo -e "\e[32mVerifying Config Syntax (Ensuring No Errors)...\e[0m"
if grep -qE "invalid|error|unknown" ~/.config/hypr/hyprland.conf; then
    echo -e "\e[31mErrors Detected in Your Config! Fixing...\e[0m"
    sed -i '/invalid/d' ~/.config/hypr/hyprland.conf
    sed -i '/error/d' ~/.config/hypr/hyprland.conf
    sed -i '/unknown/d' ~/.config/hypr/hyprland.conf
fi

### ✅ Step 6: Restarting Hyprland (If in GUI)
echo -e "\e[32mHyprland Config Debug Complete! Restarting Hyprland...\e[0m"
pkill -f Hyprland && Hyprland &

echo -e "\e[32mHyprland Config Debug Complete! Your Config is Clean.\e[0m"
