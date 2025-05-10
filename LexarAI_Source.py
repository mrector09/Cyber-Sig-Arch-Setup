
import tkinter as tk
from tkinter import scrolledtext, messagebox
import os

class LexarAI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("LexarAI - Your Windows AI Assistant")
        self.window.geometry("800x500")
        self.window.configure(bg='#1e1e2e')

        # Chat Display
        self.chat_display = scrolledtext.ScrolledText(self.window, width=85, height=20, bg='#1e1e2e', fg='#ffffff')
        self.chat_display.pack(pady=10)
        self.chat_display.insert(tk.END, "LexarAI: Hello! How can I assist you today?
")

        # User Input
        self.user_input = tk.Entry(self.window, width=70, bg='#2e2e3e', fg='#ffffff')
        self.user_input.pack(pady=5)
        self.user_input.bind("<Return>", self.get_response)

        # Send Button
        self.send_button = tk.Button(self.window, text="Send", command=self.get_response, bg='#5c5cff', fg='#ffffff')
        self.send_button.pack(pady=5)

        self.window.mainloop()

    def get_response(self, event=None):
        user_text = self.user_input.get()
        if user_text.strip() == "":
            return

        self.chat_display.insert(tk.END, f"You: {user_text}
")
        self.user_input.delete(0, tk.END)

        # Simple AI Response (Offline)
        if "hello" in user_text.lower():
            response = "Hello! How can I help you today?"
        elif "open notepad" in user_text.lower():
            os.system("notepad.exe")
            response = "I've opened Notepad for you."
        elif "shutdown" in user_text.lower():
            response = "Are you sure you want to shut down? Use the shutdown command."
        else:
            response = "I'm here to help. What would you like me to do?"

        self.chat_display.insert(tk.END, f"LexarAI: {response}
")
        self.chat_display.see(tk.END)

if __name__ == "__main__":
    LexarAI()
