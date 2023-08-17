import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)  # Update every 1000ms (1 second)

root = tk.Tk()
root.title("Digital Clock by Prabhash")
root.geometry("1000x300")  # Set the window size

label = tk.Label(root, font=("Helvetica", 48))
label.pack(pady=20)

update_time()  # Initial call to start updating time
root.mainloop()
