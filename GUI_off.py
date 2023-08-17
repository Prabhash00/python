import tkinter as tk
import os

def shutdown_windows():
    os.system("shutdown /s /t 0")

root = tk.Tk()
root.title("Windows 11 Shutdown")
root.geometry("300x100")

label = tk.Label(root, text="Click the button to shut down Windows 11.", padx=10, pady=10)
label.pack()

shutdown_button = tk.Button(root, text="Shutdown", command=shutdown_windows)
shutdown_button.pack(pady=20)

root.mainloop()
