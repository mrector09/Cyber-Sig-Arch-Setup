
# LexarWin - Advanced Windows Control Dashboard (Python Source Code)

import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import os

class LexarWin:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("LexarWin - Advanced Windows Control")
        self.window.geometry("1000x600")
        self.window.configure(bg='#1e1e2e')

        # Dashboard Tabs
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(pady=10, fill='both', expand=True)

        # System Control Tab
        self.system_tab = tk.Frame(self.notebook, bg='#2e2e3e')
        self.notebook.add(self.system_tab, text="System Control")
        self.setup_system_tab()

        # File Management Tab
        self.file_tab = tk.Frame(self.notebook, bg='#2e2e3e')
        self.notebook.add(self.file_tab, text="File Management")
        self.setup_file_tab()

        # Network Management Tab
        self.network_tab = tk.Frame(self.notebook, bg='#2e2e3e')
        self.notebook.add(self.network_tab, text="Network Management")
        self.setup_network_tab()

        # LexarAI Tab
        self.ai_tab = tk.Frame(self.notebook, bg='#2e2e3e')
        self.notebook.add(self.ai_tab, text="LexarAI")
        self.setup_ai_tab()

        self.window.mainloop()

    def setup_system_tab(self):
        tk.Label(self.system_tab, text="System Control", bg='#2e2e3e', fg='#ffffff').pack()
        self.shutdown_button = tk.Button(self.system_tab, text="Shutdown", command=self.shutdown_system, bg='#5c5cff', fg='#ffffff')
        self.shutdown_button.pack(pady=5)

        self.restart_button = tk.Button(self.system_tab, text="Restart", command=self.restart_system, bg='#5c5cff', fg='#ffffff')
        self.restart_button.pack(pady=5)

    def setup_file_tab(self):
        tk.Label(self.file_tab, text="File Management", bg='#2e2e3e', fg='#ffffff').pack()
        self.create_file_button = tk.Button(self.file_tab, text="Create File", command=self.create_file, bg='#5c5cff', fg='#ffffff')
        self.create_file_button.pack(pady=5)

    def setup_network_tab(self):
        tk.Label(self.network_tab, text="Network Management", bg='#2e2e3e', fg='#ffffff').pack()
        self.ip_label = tk.Label(self.network_tab, text="Your IP: ", bg='#2e2e3e', fg='#ffffff')
        self.ip_label.pack(pady=5)
        self.update_ip()

    def setup_ai_tab(self):
        tk.Label(self.ai_tab, text="LexarAI - Command Center", bg='#2e2e3e', fg='#ffffff').pack()
        self.ai_input = tk.Entry(self.ai_tab, width=50)
        self.ai_input.pack(pady=5)
        self.ai_button = tk.Button(self.ai_tab, text="Run Command", command=self.run_ai_command, bg='#5c5cff', fg='#ffffff')
        self.ai_button.pack(pady=5)

    def shutdown_system(self):
        os.system("shutdown /s /f /t 0")

    def restart_system(self):
        os.system("shutdown /r /f /t 0")

    def create_file(self):
        with open("NewFile.txt", "w") as file:
            file.write("This is a new file created by LexarWin.")

    def update_ip(self):
        self.ip_label.config(text="Your IP: " + os.popen("ipconfig").read().split("IPv4")[1].split(":")[1].split()[0])

    def run_ai_command(self):
        command = self.ai_input.get()
        os.system(command)
        messagebox.showinfo("Command Executed", f"Executed: {command}")

if __name__ == "__main__":
    LexarWin()
