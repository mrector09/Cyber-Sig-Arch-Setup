
#!/bin/bash

echo "Starting Opera Privacy Configuration on Arch Linux..."

# Ensure the system is updated
sudo pacman -Syu --noconfirm

# Install Opera Browser if not already installed
sudo pacman -S opera --noconfirm

# Launch Opera to create initial configuration files
opera &
sleep 5
pkill opera

# Configure Privacy Settings
echo "Configuring Privacy and Security Settings..."

# Configuring Secure DNS (Cloudflare)
sed -i 's/"dns_over_https": false/"dns_over_https": true/g' ~/.config/opera/Preferences
sed -i 's/"dns_over_https_provider": ""/"dns_over_https_provider": "https:\/\/1.1.1.1\/dns-query"/g' ~/.config/opera/Preferences

# Block Third-Party Cookies
sed -i 's/"block_third_party_cookies": false/"block_third_party_cookies": true/g' ~/.config/opera/Preferences

# Enable Do Not Track
sed -i 's/"do_not_track": false/"do_not_track": true/g' ~/.config/opera/Preferences

# Block Dangerous Content
sed -i 's/"safebrowsing_enabled": false/"safebrowsing_enabled": true/g' ~/.config/opera/Preferences

# Install Recommended Privacy Extensions
echo "Installing Recommended Privacy Extensions..."
opera "https://addons.opera.com/en/extensions/details/ublock/" &
sleep 3
pkill opera

opera "https://addons.opera.com/en/extensions/details/https-everywhere/" &
sleep 3
pkill opera

opera "https://addons.opera.com/en/extensions/details/privacy-badger/" &
sleep 3
pkill opera

opera "https://addons.opera.com/en/extensions/details/duckduckgo-privacy-essentials/" &
sleep 3
pkill opera

echo "Opera Privacy Configuration Completed."
echo "Launch Opera with: opera"
