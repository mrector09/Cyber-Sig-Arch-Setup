
#!/bin/bash

echo "Starting Complete System Cleanup for Hyprland..."

# 1. Stop Hyprland and clean existing configs
echo "Stopping Hyprland and Cleaning Existing Configs..."
pkill Hyprland
rm -rf ~/.config/hypr ~/.config/waybar ~/.config/kitty ~/.config/rofi ~/.config/neofetch ~/.config/swaylock
rm -rf ~/.local/share/hypr ~/.local/state/hypr

# 2. Uninstall Hyprland and related packages
echo "Uninstalling Hyprland and Related Packages..."
sudo pacman -Rns hyprland waybar rofi kitty swaylock neofetch -y

# 3. Clear Package Cache and Refresh Repositories
echo "Clearing Package Cache and Refreshing Repositories..."
sudo pacman -Scc --noconfirm
sudo pacman -Syyu --noconfirm

# 4. Reinstall Hyprland and Essential Packages
echo "Reinstalling Hyprland and Essential Packages..."
sudo pacman -S hyprland waybar rofi kitty swaylock neofetch --noconfirm

# 5. Downloading a Stable, Pre-Built Hyprland Dotfile Configuration (Community Dotfiles)
echo "Downloading Stable Community Dotfiles..."
git clone https://github.com/hyprland-community/hyprland-dotfiles.git ~/hyprland-dotfiles
cp -r ~/hyprland-dotfiles/* ~/.config/

# 6. Setting Up Basic Configurations for Stability
echo "Setting Up Basic Configurations..."
mkdir -p ~/.config/hypr
mkdir -p ~/.config/waybar
mkdir -p ~/.config/rofi
mkdir -p ~/.config/kitty
mkdir -p ~/.config/neofetch
mkdir -p ~/.config/swaylock

cp ~/.config/hyprland-dotfiles/hypr/hyprland.conf ~/.config/hypr/
cp ~/.config/hyprland-dotfiles/waybar/waybar.json ~/.config/waybar/
cp ~/.config/hyprland-dotfiles/kitty/kitty.conf ~/.config/kitty/
cp ~/.config/hyprland-dotfiles/neofetch/config.conf ~/.config/neofetch/
cp ~/.config/hyprland-dotfiles/swaylock/config ~/.config/swaylock/

# 7. Restarting System
echo "System Reset Complete. Rebooting Now..."
reboot
