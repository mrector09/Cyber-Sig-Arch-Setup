
#!/bin/bash

echo "========================================="
echo "  Installing Lexarv6 AI and Hyprland... "
echo "========================================="

# Updating system packages
sudo pacman -Syu --noconfirm

# Installing essential dependencies
sudo pacman -S git curl wget neovim rofi waybar hyprland eww kitty alacritty zsh --noconfirm

# Setting up Hyprland Dotfiles (Stable Configuration)
echo "Cloning and setting up Hyprland dotfiles..."
git clone https://github.com/mylinuxforwork/dotfiles.git ~/.config/hyprland
cd ~/.config/hyprland
chmod +x setup-arch.sh
./setup-arch.sh

# Setting up Lexarv6 AI System
echo "Installing Lexarv6 AI..."
mkdir -p ~/.lexar
wget -O ~/.lexar/lexarv6.py https://sandbox:/mnt/data/lexarv6.py
chmod +x ~/.lexar/lexarv6.py

# Creating a startup alias for Lexarv6
echo "alias lexar='python3 ~/.lexar/lexarv6.py'" >> ~/.zshrc
echo "alias lexar='python3 ~/.lexar/lexarv6.py'" >> ~/.bashrc
source ~/.zshrc
source ~/.bashrc

# Setting Hyprland as the default session in LightDM (Display Manager)
sudo systemctl enable lightdm.service
sudo systemctl start lightdm.service

# Providing instructions to launch Hyprland
echo "==========================================="
echo "  Lexarv6 and Hyprland Installation Complete"
echo "==========================================="
echo "To run Lexarv6 AI, simply type 'lexar' in your terminal."
echo "To launch Hyprland, choose 'Hyprland' from the display manager (LightDM)."
