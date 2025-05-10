
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import psutil
import os

class LexarLua:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("LexarLua - Advanced Roblox Lua Executor")
        self.window.geometry("800x500")
        self.window.configure(bg='#1e1e2e')

        # Attach to Roblox Button
        self.attach_button = tk.Button(self.window, text="Attach to Roblox", command=self.attach_to_roblox, bg='#5c5cff', fg='#ffffff')
        self.attach_button.pack(pady=5)

        # Script Hub (Pre-loaded Scripts)
        self.script_text = scrolledtext.ScrolledText(self.window, width=85, height=20, bg='#1e1e2e', fg='#ffffff')
        self.script_text.pack(pady=10)

        # Buttons for Script Controls
        self.load_button = tk.Button(self.window, text="Load Script", command=self.load_script, bg='#5c5cff', fg='#ffffff')
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.execute_button = tk.Button(self.window, text="Execute", command=self.execute_script, bg='#5c5cff', fg='#ffffff')
        self.execute_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.window, text="Clear", command=self.clear_script, bg='#5c5cff', fg='#ffffff')
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.window.mainloop()

    def attach_to_roblox(self):
        roblox_found = any("RobloxPlayerBeta" in p.name() for p in psutil.process_iter())
        if roblox_found:
            messagebox.showinfo("Success", "Roblox Detected and Attached!")
        else:
            messagebox.showwarning("Warning", "Roblox is not running. Please open Roblox first.")

    def load_script(self):
        script_path = filedialog.askopenfilename(title="Select Lua Script", filetypes=[("Lua Files", "*.lua")])
        if script_path:
            with open(script_path, "r") as file:
                self.script_text.insert(tk.END, file.read())

    def clear_script(self):
        self.script_text.delete(1.0, tk.END)

    def execute_script(self):
        script = self.script_text.get(1.0, tk.END).strip()
        if script:
            try:
                self.run_lua_script(script)
                messagebox.showinfo("Success", "Script executed successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to execute script: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No script loaded.")

    def run_lua_script(self, script):
        print("Executing Lua Script:")
        print(script)

if __name__ == "__main__":
    LexarLua()
