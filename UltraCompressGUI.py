
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

class UltraCompressGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("UltraCompress - Maximum Compression Tool")
        self.window.geometry("500x300")
        self.window.configure(bg='#1e1e2e')

        # File Selection
        self.file_label = tk.Label(self.window, text="Select File or Folder to Compress:", bg='#1e1e2e', fg='#ffffff')
        self.file_label.pack(pady=5)

        self.file_path = tk.Entry(self.window, width=40, bg='#2e2e3e', fg='#ffffff')
        self.file_path.pack(pady=5)

        self.browse_button = tk.Button(self.window, text="Browse", command=self.browse_file, bg='#5c5cff', fg='#ffffff')
        self.browse_button.pack(pady=5)

        # Compress Button
        self.compress_button = tk.Button(self.window, text="Compress to 25 MB", command=self.compress_file, bg='#5c5cff', fg='#ffffff')
        self.compress_button.pack(pady=10)

        self.status_label = tk.Label(self.window, text="", bg='#1e1e2e', fg='#ffffff')
        self.status_label.pack(pady=5)

        self.window.mainloop()

    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Select File or Folder")
        if file_path:
            self.file_path.delete(0, tk.END)
            self.file_path.insert(0, file_path)

    def compress_file(self):
        target = self.file_path.get()
        if not target:
            messagebox.showwarning("Warning", "Please select a file or folder to compress.")
            return

        self.status_label.config(text="Compressing... Please wait.")
        self.window.update()

        output = "UltraCompressed.7z"
        try:
            # Running 7-Zip with maximum compression
            result = subprocess.run(
                ["7z", "a", "-t7z", "-mx=9", "-m0=lzma2", "-mfb=273", "-md=1536m", "-ms=on", output, target],
                capture_output=True, text=True
            )
            file_size = os.path.getsize(output)

            # Check if size exceeds 25 MB (26214400 bytes)
            if file_size > 26214400:
                self.status_label.config(text="Re-compressing to reduce size...")
                self.window.update()

                subprocess.run(
                    ["7z", "a", "-t7z", "-mx=9", "-m0=lzma2", "-md=1024m", "-ms=on", output, target]
                )
                file_size = os.path.getsize(output)

            if file_size <= 26214400:
                self.status_label.config(text="Compression complete. File is under 25 MB.")
                messagebox.showinfo("Success", f"File compressed to {round(file_size / 1024 / 1024, 2)} MB")
            else:
                self.status_label.config(text="Compression complete, but file exceeds 25 MB.")
                messagebox.showwarning("Warning", "File still exceeds 25 MB.")

        except Exception as e:
            messagebox.showerror("Error", f"Compression failed: {str(e)}")

if __name__ == "__main__":
    UltraCompressGUI()
