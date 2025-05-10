
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Initialize the main application window
app = tk.Tk()
app.title("LexarLua - Advanced Roblox Lua Executor")
app.geometry("800x500")
app.configure(bg="#1e1e2e")

# Sidebar (Navigation)
sidebar = tk.Frame(app, width=200, height=500, bg="#2e2e3e")
sidebar.pack(side="left", fill="y")

# Function to switch main panel content
def show_panel(panel_name):
    for widget in main_panel.winfo_children():
        widget.destroy()
    
    if panel_name == "Script Hub":
        tk.Label(main_panel, text="Script Hub", font=("Arial", 18), bg="#1e1e2e", fg="#ffffff").pack(pady=20)
        script_text = scrolledtext.ScrolledText(main_panel, width=60, height=20, bg="#2e2e3e", fg="#ffffff")
        script_text.pack()

        def execute_script():
            script = script_text.get("1.0", "end")
            messagebox.showinfo("Execution", "Script executed (simulated).")

        execute_button = tk.Button(main_panel, text="Execute Script", command=execute_script, bg="#5c5cff", fg="#ffffff")
        execute_button.pack(pady=5)
    
    elif panel_name == "LexarAI":
        tk.Label(main_panel, text="LexarAI - Command Center", font=("Arial", 18), bg="#1e1e2e", fg="#ffffff").pack(pady=20)
        ai_input = tk.Entry(main_panel, width=50)
        ai_input.pack(pady=5)
        
        def run_ai_command():
            command = ai_input.get()
            messagebox.showinfo("LexarAI", f"Command received: {command} (simulated).")

        run_button = tk.Button(main_panel, text="Run Command", command=run_ai_command, bg="#5c5cff", fg="#ffffff")
        run_button.pack(pady=5)

    elif panel_name == "Settings":
        tk.Label(main_panel, text="Settings", font=("Arial", 18), bg="#1e1e2e", fg="#ffffff").pack(pady=20)

# Sidebar Buttons
buttons = [("Script Hub", "Script Hub"), ("LexarAI", "LexarAI"), ("Settings", "Settings")]
for text, panel in buttons:
    btn = tk.Button(sidebar, text=text, command=lambda p=panel: show_panel(p), bg="#3e3e4e", fg="#ffffff")
    btn.pack(fill="x", pady=5)

# Main Panel (Dynamic Content)
main_panel = tk.Frame(app, width=580, height=500, bg="#1e1e2e")
main_panel.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Load Script Hub by Default
show_panel("Script Hub")

# Run the Application
app.mainloop()
