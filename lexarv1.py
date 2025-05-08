
import curses
import subprocess
import time
import os

def speak(message):
    try:
        # Using mpg123 with pre-recorded voice clips (offline, fast, reliable)
        subprocess.run(["mpg123", f"/usr/local/share/lexar/voice/{message}.mp3"])
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
            speak("blast_off")
            subprocess.run(["bash", "-c", "./lexar.sh"])
            speak("blast_off_complete")

        elif choice == ord('2'):
            stdscr.addstr(14, 2, "Running Full Diagnostic and Auto-Repair...")
            speak("diagnostic_start")
            subprocess.run(["bash", "-c", "lexar_ai 'config_error' && lexar_ai 'package_error' && lexar_ai 'dependency_error'"])
            speak("diagnostic_complete")

        elif choice == ord('3'):
            stdscr.addstr(14, 2, "Fixing Configuration Errors...")
            speak("config_fix_start")
            subprocess.run(["bash", "-c", "lexar_ai 'config_error'"])
            speak("config_fix_complete")

        elif choice == ord('4'):
            stdscr.addstr(14, 2, "Fixing Package Errors (PGP, Dependencies)...")
            speak("package_fix_start")
            subprocess.run(["bash", "-c", "lexar_ai 'package_error' && lexar_ai 'pgp_error'"])
            speak("package_fix_complete")

        elif choice == ord('5'):
            stdscr.addstr(14, 2, "Restarting Network...")
            speak("network_restart")
            subprocess.run(["bash", "-c", "lexar_ai 'network_error'"])
            speak("network_restart_complete")

        elif choice == ord('6'):
            stdscr.addstr(14, 2, "Repairing Login Loop...")
            speak("login_loop_fix")
            subprocess.run(["bash", "-c", "lexar_ai 'login_loop'"])
            speak("login_loop_complete")

        elif choice == ord('7'):
            stdscr.addstr(14, 2, "Clearing RAM Cache...")
            speak("ram_clear")
            subprocess.run(["bash", "-c", "lexar_ai 'ram_error'"])
            speak("ram_clear_complete")

        elif choice == ord('8'):
            stdscr.addstr(14, 2, "Optimizing CPU Performance...")
            speak("cpu_optimize")
            subprocess.run(["bash", "-c", "lexar_ai 'cpu_overload'"])
            speak("cpu_optimize_complete")

        elif choice == ord('9'):
            stdscr.addstr(14, 2, "Running Disk Repair (Filesystem Check)...")
            speak("disk_repair")
            subprocess.run(["bash", "-c", "lexar_ai 'disk_error'"])
            speak("disk_repair_complete")

        elif choice == ord('0'):
            stdscr.addstr(14, 2, "Exiting Lexar TUI...")
            speak("exit")
            time.sleep(1)
            break

        stdscr.refresh()
        time.sleep(1)

curses.wrapper(lexar_tui)
