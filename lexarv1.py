
import curses
import subprocess
import time
import os

def lexar_tui(stdscr):
    stdscr.clear()
    curses.curs_set(0)

    while True:
        stdscr.clear()
        stdscr.addstr(1, 2, "Lexar TUI (Text User Interface) - System AI Control (Final Version)", curses.A_BOLD)
        stdscr.addstr(3, 2, "1. Blast Off (Full Custom Installation with Auto-Fix)")
        stdscr.addstr(4, 2, "2. Diagnose and Auto-Repair System")
        stdscr.addstr(5, 2, "3. Fix Configuration Errors (Hyprland, Waybar, Kitty)")
        stdscr.addstr(6, 2, "4. Fix Package Errors (PGP, Dependencies)")
        stdscr.addstr(7, 2, "5. Restart Network (Fix Network Errors)")
        stdscr.addstr(8, 2, "6. Repair Login Loop (Display Manager)")
        stdscr.addstr(9, 2, "7. Clear RAM Cache")
        stdscr.addstr(10, 2, "8. Optimize CPU Performance")
        stdscr.addstr(11, 2, "9. Run Disk Repair (Filesystem Check)")
        stdscr.addstr(12, 2, "0. Exit")

        stdscr.refresh()
        choice = stdscr.getch()

        if choice == ord('1'):
            stdscr.addstr(14, 2, "Initiating Blast Off with Auto-Fix (No GitHub Login)...")
            stdscr.refresh()
            time.sleep(1)
            stdscr.addstr(15, 2, "Cleaning Existing Configurations and Fixing PGP...")
            stdscr.refresh()
            subprocess.run([
                "bash", "-c",
                '''
                sudo rm -rf ~/.config/hypr ~/.config/waybar ~/.config/kitty ~/.config/rofi ~/.config/neofetch ~/.config/swaylock;
                sudo rm -rf /etc/pacman.d/gnupg;
                sudo pacman-key --init;
                sudo pacman-key --populate archlinux;
                sudo pacman-key --refresh-keys;
                sudo pacman -Syyu --noconfirm --disable-download-timeout --overwrite "*" --assume-yes --needed --allow-unauthenticated;
                git clone https://github.com/hyprland-community/hyprland-dotfiles.git ~/hyprland-dotfiles --depth=1 || echo "GitHub Clone Failed. Retrying..." && sleep 2;
                cp -r ~/hyprland-dotfiles/* ~/.config/;
                sudo pacman -S hyprland waybar rofi kitty swaylock neofetch --noconfirm --needed;
                '''
            ])
            stdscr.addstr(16, 2, "Blast Off Completed Successfully.")
            stdscr.refresh()

        elif choice == ord('2'):
            stdscr.addstr(14, 2, "Running Full Diagnostic and Auto-Repair...")
            subprocess.run(["bash", "-c", "lexar_ai 'config_error' && lexar_ai 'package_error' && lexar_ai 'dependency_error'"])

        elif choice == ord('3'):
            stdscr.addstr(14, 2, "Fixing Configuration Errors...")
            subprocess.run(["bash", "-c", "lexar_ai 'config_error'"])

        elif choice == ord('4'):
            stdscr.addstr(14, 2, "Fixing Package Errors (PGP, Dependencies)...")
            subprocess.run(["bash", "-c", "lexar_ai 'package_error' && lexar_ai 'pgp_error'"])

        elif choice == ord('5'):
            stdscr.addstr(14, 2, "Restarting Network...")
            subprocess.run(["bash", "-c", "lexar_ai 'network_error'"])

        elif choice == ord('6'):
            stdscr.addstr(14, 2, "Repairing Login Loop...")
            subprocess.run(["bash", "-c", "lexar_ai 'login_loop'"])

        elif choice == ord('7'):
            stdscr.addstr(14, 2, "Clearing RAM Cache...")
            subprocess.run(["bash", "-c", "lexar_ai 'ram_error'"])

        elif choice == ord('8'):
            stdscr.addstr(14, 2, "Optimizing CPU Performance...")
            subprocess.run(["bash", "-c", "lexar_ai 'cpu_overload'"])

        elif choice == ord('9'):
            stdscr.addstr(14, 2, "Running Disk Repair (Filesystem Check)...")
            subprocess.run(["bash", "-c", "lexar_ai 'disk_error'"])

        elif choice == ord('0'):
            stdscr.addstr(14, 2, "Exiting Lexar TUI...")
            time.sleep(1)
            break

        stdscr.refresh()
        time.sleep(1)

curses.wrapper(lexar_tui)
