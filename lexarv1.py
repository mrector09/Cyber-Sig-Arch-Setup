
import curses
import subprocess
import time
import os

def lexar_tui(stdscr):
    stdscr.clear()
    curses.curs_set(0)

    while True:
        stdscr.clear()
        stdscr.addstr(1, 2, "Lexar TUI (Text User Interface) - System AI Control (Advanced)", curses.A_BOLD)
        stdscr.addstr(3, 2, "1. Diagnose and Auto-Repair System")
        stdscr.addstr(4, 2, "2. Fix Configuration Errors (Hyprland, Waybar, Kitty)")
        stdscr.addstr(5, 2, "3. Fix Package Errors (PGP, Dependencies)")
        stdscr.addstr(6, 2, "4. Restart Network (Fix Network Errors)")
        stdscr.addstr(7, 2, "5. Repair Login Loop (Display Manager)")
        stdscr.addstr(8, 2, "6. Clear RAM Cache")
        stdscr.addstr(9, 2, "7. Optimize CPU Performance")
        stdscr.addstr(10, 2, "8. Run Disk Repair (Filesystem Check)")
        stdscr.addstr(11, 2, "9. View System Logs")
        stdscr.addstr(12, 2, "0. Exit")

        stdscr.refresh()
        choice = stdscr.getch()

        if choice == ord('1'):
            stdscr.addstr(14, 2, "Running Full Diagnostic and Auto-Repair...")
            os.system("espeak 'Running full diagnostic and auto-repair.'")
            subprocess.run(["bash", "-c", "lexar_ai 'config_error' && lexar_ai 'package_error' && lexar_ai 'dependency_error'"])

        elif choice == ord('2'):
            stdscr.addstr(14, 2, "Fixing Configuration Errors...")
            os.system("espeak 'Fixing configuration errors.'")
            subprocess.run(["bash", "-c", "lexar_ai 'config_error'"])

        elif choice == ord('3'):
            stdscr.addstr(14, 2, "Fixing Package Errors (PGP, Dependencies)...")
            os.system("espeak 'Fixing package and PGP errors.'")
            subprocess.run(["bash", "-c", "lexar_ai 'package_error' && lexar_ai 'pgp_error'"])

        elif choice == ord('4'):
            stdscr.addstr(14, 2, "Restarting Network...")
            os.system("espeak 'Restarting network services.'")
            subprocess.run(["bash", "-c", "lexar_ai 'network_error'"])

        elif choice == ord('5'):
            stdscr.addstr(14, 2, "Repairing Login Loop...")
            os.system("espeak 'Repairing login loop.'")
            subprocess.run(["bash", "-c", "lexar_ai 'login_loop'"])

        elif choice == ord('6'):
            stdscr.addstr(14, 2, "Clearing RAM Cache...")
            os.system("espeak 'Clearing RAM cache.'")
            subprocess.run(["bash", "-c", "lexar_ai 'ram_error'"])

        elif choice == ord('7'):
            stdscr.addstr(14, 2, "Optimizing CPU Performance...")
            os.system("espeak 'Optimizing CPU performance.'")
            subprocess.run(["bash", "-c", "lexar_ai 'cpu_overload'"])

        elif choice == ord('8'):
            stdscr.addstr(14, 2, "Running Disk Repair (Filesystem Check)...")
            os.system("espeak 'Running disk repair.'")
            subprocess.run(["bash", "-c", "lexar_ai 'disk_error'"])

        elif choice == ord('9'):
            stdscr.addstr(14, 2, "Displaying System Logs...")
            logs = subprocess.getoutput("journalctl -xe | tail -n 20")
            stdscr.addstr(16, 2, logs)
            stdscr.refresh()
            stdscr.getch()

        elif choice == ord('0'):
            stdscr.addstr(14, 2, "Exiting Lexar TUI...")
            os.system("espeak 'Exiting Lexar interface.'")
            time.sleep(1)
            break

        stdscr.refresh()
        time.sleep(1)

curses.wrapper(lexar_tui)
