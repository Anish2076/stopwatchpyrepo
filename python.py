import tkinter as tk
from time import strftime

class ClockStopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock & Stopwatch")
        self.root.geometry("400x350")
        self.root.configure(bg="#121212")
        self.root.resizable(False, False)

        # ----------- Digital Clock Section -----------
        clock_title = tk.Label(root, text="🕒 Digital Clock", font=("Helvetica", 16, "bold"), bg="#121212", fg="#00cec9")
        clock_title.pack(pady=(10, 5))

        self.clock_label = tk.Label(root, font=("Helvetica", 36, "bold"), fg="#00d2d3", bg="#121212")
        self.clock_label.pack()

        self.update_clock()

        # ----------- Divider -----------
        divider = tk.Label(root, text="⏱️ Stopwatch", font=("Helvetica", 16, "bold"), bg="#121212", fg="#ff7675")
        divider.pack(pady=(30, 5))

        # ----------- Stopwatch Section -----------
        self.time = 0
        self.running = False

        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Helvetica", 36, "bold"), fg="#fab1a0", bg="#121212")
        self.stopwatch_label.pack(pady=10)

        btn_frame = tk.Frame(root, bg="#121212")
        btn_frame.pack(pady=5)

        # Buttons
        start_btn = tk.Button(btn_frame, text="Start", width=10, bg="#00b894", fg="white", font=("Helvetica", 11, "bold"), command=self.start)
        stop_btn = tk.Button(btn_frame, text="Stop", width=10, bg="#d63031", fg="white", font=("Helvetica", 11, "bold"), command=self.stop)
        reset_btn = tk.Button(btn_frame, text="Reset", width=10, bg="#636e72", fg="white", font=("Helvetica", 11, "bold"), command=self.reset)

        start_btn.grid(row=0, column=0, padx=5)
        stop_btn.grid(row=0, column=1, padx=5)
        reset_btn.grid(row=0, column=2, padx=5)

    # ---------- Clock Logic ----------
    def update_clock(self):
        current_time = strftime('%I:%M:%S %p')
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

    # ---------- Stopwatch Logic ----------
    def update_stopwatch(self):
        if self.running:
            self.time += 1
            mins, secs = divmod(self.time, 60)
            hrs, mins = divmod(mins, 60)
            self.stopwatch_label.config(text=f"{hrs:02}:{mins:02}:{secs:02}")
            self.root.after(1000, self.update_stopwatch)

    def start(self):
        if not self.running:
            self.running = True
            self.update_stopwatch()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time = 0
        self.stopwatch_label.config(text="00:00:00")

# --------- Run App ---------
if __name__ == "__main__":
    root = tk.Tk()
    app = ClockStopwatchApp(root)
    root.mainloop()
