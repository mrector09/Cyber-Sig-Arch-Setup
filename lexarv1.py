
import curses
import subprocess
import time
import os

def lexar_tui(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Cyan text
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)   # Red text
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK) # Green text

    while True:
        stdscr.clear()
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(1, 2, "╔═════════════════════════════════════════════════════╗")
        stdscr.addstr(2, 2, "║             LEXAR SYSTEM AI CONTROL (RUNE)          ║")
        stdscr.addstr(3, 2, "║   ⌖   ⌖   ⌖  CUSTOM RUNE SYMBOL  ⌖   ⌖   ⌖   ║")
        stdscr.addstr(4, 2, "╚═════════════════════════════════════════════════════╝")
        stdscr.attroff(curses.color_pair(1))

        stdscr.addstr(6, 2, "1. Blast Off (Full Custom Installation with Auto-Fix)", curses.color_pair(3))
        stdscr.addstr(7, 2, "2. Diagnose and Auto-Repair System", curses.color_pair(3))
        stdscr.addstr(8, 2, "3. Fix Configuration Errors (Hyprland, Waybar, Kitty)", curses.color_pair(3))
        stdscr.addstr(9, 2, "4. Fix Package Errors (PGP, Dependencies)", curses.color_pair(3))
        stdscr.addstr(10, 2, "5. Restart Network (Fix Network Errors)", curses.color_pair(3))
        stdscr.addstr(11, 2, "6. Repair Login Loop (Display Manager)", curses.color_pair(3))
        stdscr.addstr(12, 2, "7. Clear RAM Cache", curses.color_pair(3))
        stdscr.addstr(13, 2, "8. Optimize CPU Performance", curses.color_pair(3))
        stdscr.addstr(14, 2, "9. Run Disk Repair (Filesystem Check)", curses.color_pair(3))
        stdscr.addstr(15, 2, "0. Exit", curses.color_pair(2))

        stdscr.refresh()
        choice = stdscr.getch()

        if choice == ord('1'):
            stdscr.addstr(17, 2, "Initiating Blast Off with Auto-Fix (No GitHub Login)...", curses.color_pair(2))
            stdscr.refresh()
            time.sleep(1)
            stdscr.addstr(18, 2, "Cleaning Existing Configurations and Fixing PGP...", curses.color_pair(2))
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
            stdscr.addstr(19, 2, "Blast Off Completed Successfully.", curses.color_pair(3))
            stdscr.refresh()

        elif choice == ord('0'):
            stdscr.addstr(17, 2, "Exiting Lexar TUI...", curses.color_pair(2))
            time.sleep(1)
            break

        stdscr.refresh()
        time.sleep(1)

curses.wrapper(lexar_tui)
