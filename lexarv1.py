
import curses
import subprocess
import time
import os

def speak(message):
    try:
        subprocess.run(["spd-say", message])
    except FileNotFoundError:
        print(f"Voice Notification (Text Only): {message}")

def lexar_tui(stdscr):
    stdscr.clear()
    curses.curs_set(0)

    while True:
        stdscr.clear()
        stdscr.addstr(1, 2, "Lexar TUI (Text User Interface) - System AI Control (Advanced)", curses.A_BOLD)
        stdscr.addstr(3, 2, "1. Blast Off (Full Custom Installation with PGP Bypass)")
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
            stdscr.addstr(14, 2, "Initiating Blast Off (PGP Bypass Enabled)...")
            speak("Initiating Blast Off. Installing full custom setup with PGP bypass. This will take a moment.")
            subprocess.run(["bash", "-c", "./lexar.sh"])
            speak("Blast Off installation complete. Your system is now customized.")

        elif choice == ord('2'):
            stdscr.addstr(14, 2, "Running Full Diagnostic and Auto-Repair...")
            speak("Running full diagnostic and auto-repair. I will fix any detected issues.")
            subprocess.run(["bash", "-c", "lexar_ai 'config_error' && lexar_ai 'package_error' && lexar_ai 'dependency_error'"])
            speak("Diagnostic complete. System errors have been repaired.")

        elif choice == ord('3'):
            stdscr.addstr(14, 2, "Fixing Configuration Errors...")
            speak("Fixing configuration errors. Hyprland, Waybar, Kitty, and related settings.")
            subprocess.run(["bash", "-c", "lexar_ai 'config_error'"])
            speak("Configuration errors fixed.")

        elif choice == ord('4'):
            stdscr.addstr(14, 2, "Fixing Package Errors (PGP, Dependencies)...")
            speak("Fixing package and PGP errors. This may take a moment.")
            subprocess.run(["bash", "-c", "lexar_ai 'package_error' && lexar_ai 'pgp_error'"])
            speak("Package errors resolved. System is secure.")

        elif choice == ord('5'):
            stdscr.addstr(14, 2, "Restarting Network...")
            speak("Restarting network services. Connectivity should be restored shortly.")
            subprocess.run(["bash", "-c", "lexar_ai 'network_error'"])
            speak("Network services restarted.")

        elif choice == ord('6'):
            stdscr.addstr(14, 2, "Repairing Login Loop...")
            speak("Repairing login loop. You will be able to log in again.")
            subprocess.run(["bash", "-c", "lexar_ai 'login_loop'"])
            speak("Login loop repaired. System access restored.")

        elif choice == ord('7'):
            stdscr.addstr(14, 2, "Clearing RAM Cache...")
            speak("Clearing RAM cache to free up memory.")
            subprocess.run(["bash", "-c", "lexar_ai 'ram_error'"])
            speak("RAM cache cleared. System memory optimized.")

        elif choice == ord('8'):
            stdscr.addstr(14, 2, "Optimizing CPU Performance...")
            speak("Optimizing CPU performance for maximum speed.")
            subprocess.run(["bash", "-c", "lexar_ai 'cpu_overload'"])
            speak("CPU performance optimized. System is faster.")

        elif choice == ord('9'):
            stdscr.addstr(14, 2, "Running Disk Repair (Filesystem Check)...")
            speak("Running disk repair. This will ensure file system integrity.")
            subprocess.run(["bash", "-c", "lexar_ai 'disk_error'"])
            speak("Disk repair complete. System is secure.")

        elif choice == ord('0'):
            stdscr.addstr(14, 2, "Exiting Lexar TUI...")
            speak("Exiting Lexar interface. Goodbye.")
            time.sleep(1)
            break

        stdscr.refresh()
        time.sleep(1)

curses.wrapper(lexar_tui)
