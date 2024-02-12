import tkinter as tk
import time

class DigitalClockHoursMinutes:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock (Hours and Minutes)")
        self.root.geometry("300x100")
        self.root.configure(background="blue")

        self.time_label = tk.Label(self.root, font=("Helvetica", 24), bg="white")
        self.time_label.pack(pady=20)

        self.update_time()

    def update_time(self):
        current_time = time.localtime()
        time_str = time.strftime("%H:%M", current_time)
        self.time_label.config(text=time_str)
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClockHoursMinutes(root)
    root.mainloop()
