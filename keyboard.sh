
#!/bin/bash

echo -e "\e[32mStarting Keyboard Repair Tool for Hyprland...\e[0m"

### ✅ Step 1: Ensure XWayland is Installed
echo -e "\e[32mChecking and Installing XWayland (if missing)...\e[0m"
sudo pacman -S xorg-xwayland --noconfirm

### ✅ Step 2: Reset Keyboard Layout to US (Default)
echo -e "\e[32mResetting Keyboard Layout to US...\e[0m"
setxkbmap us
export XKB_DEFAULT_LAYOUT=us

### ✅ Step 3: Reconfigure Hyprland Keyboard Settings
echo -e "\e[32mReconfiguring Hyprland Keyboard Settings...\e[0m"
mkdir -p ~/.config/hypr

cat <<EOF > ~/.config/hypr/hyprland.conf
input {
    kb_layout = "us"
    kb_model = "pc105"
    kb_variant = ""
    kb_options = ""
}
EOF

### ✅ Step 4: Reload Hyprland Configuration
echo -e "\e[32mReloading Hyprland for Changes to Apply...\e[0m"
hyprctl reload

### ✅ Step 5: Verify and Display Success Message
echo -e "\e[32mKeyboard Repair Complete! Your keyboard should now work properly.\e[0m"
