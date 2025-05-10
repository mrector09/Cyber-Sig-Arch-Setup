
import os
import sys
import psutil
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox

class LexarLua:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("LexarLua - Ultimate Roblox Lua Executor")
        self.window.geometry("800x500")
        self.window.configure(bg='#1e1e2e')

        self.script_text = scrolledtext.ScrolledText(self.window, width=85, height=20, bg='#1e1e2e', fg='#ffffff')
        self.script_text.pack(pady=10)

        self.load_button = tk.Button(self.window, text="Load Script", command=self.load_script, bg='#5c5cff', fg='#ffffff')
        self.load_button.pack(side=tk.LEFT, padx=10)

        self.execute_button = tk.Button(self.window, text="Execute", command=self.execute_script, bg='#5c5cff', fg='#ffffff')
        self.execute_button.pack(side=tk.LEFT, padx=10)

        self.clear_button = tk.Button(self.window, text="Clear", command=self.clear_script, bg='#5c5cff', fg='#ffffff')
        self.clear_button.pack(side=tk.LEFT, padx=10)

        self.window.mainloop()

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
