
#!/bin/bash

echo "======================================="
echo "    Lexarv6 Automatic Installer"
echo "======================================="

# Creating the Lexar directory
mkdir -p ~/.lexar

# Downloading the latest version of Lexarv6
echo "Downloading Lexarv6..."
curl -L -o ~/.lexar/lexarv6.py https://sandbox:/mnt/data/lexarv6.py

# Making Lexarv6 executable
chmod +x ~/.lexar/lexarv6.py

# Creating persistent alias for Lexar
echo "Creating Lexar command alias..."
echo "alias lexar='python3 ~/.lexar/lexarv6.py'" >> ~/.bashrc
echo "alias lexar='python3 ~/.lexar/lexarv6.py'" >> ~/.zshrc

# Reloading shell configurations
source ~/.bashrc
source ~/.zshrc

# Verifying installation
echo "Verifying Lexarv6 installation..."
if [ -f ~/.lexar/lexarv6.py ]; then
    echo "✅ Lexarv6 successfully installed."
    echo "You can now run it using the command: lexar"
else
    echo "❌ Installation failed. Please try again."
fi
