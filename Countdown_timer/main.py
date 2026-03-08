import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Cool Countdown Timer")
        self.root.geometry("400x300")
        self.root.configure(bg="#2E3440")

        # Timer display
        self.timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48), fg="#88C0D0", bg="#2E3440")
        self.timer_label.pack(pady=20)

        # Input frame
        input_frame = tk.Frame(root, bg="#2E3440")
        input_frame.pack(pady=10)

        self.time_entry = tk.Entry(input_frame, font=("Helvetica", 16), width=10, justify="center")
        self.time_entry.pack(side=tk.LEFT, padx=5)
        self.time_entry.insert(0, "60")  # Default 60 seconds

        tk.Label(input_frame, text="seconds", font=("Helvetica", 14), fg="#D8DEE9", bg="#2E3440").pack(side=tk.LEFT)

        # Buttons frame
        button_frame = tk.Frame(root, bg="#2E3440")
        button_frame.pack(pady=20)

        self.start_button = tk.Button(button_frame, text="Start", command=self.start_countdown, font=("Helvetica", 14), bg="#A3BE8C", fg="#2E3440", width=8)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_countdown, font=("Helvetica", 14), bg="#BF616A", fg="#2E3440", width=8, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_timer, font=("Helvetica", 14), bg="#EBCB8B", fg="#2E3440", width=8)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.running = False
        self.remaining_time = 0

    def start_countdown(self):
        if not self.running:
            try:
                self.remaining_time = int(self.time_entry.get())
                if self.remaining_time <= 0:
                    raise ValueError
                self.running = True
                self.start_button.config(state=tk.DISABLED)
                self.stop_button.config(state=tk.NORMAL)
                self.time_entry.config(state=tk.DISABLED)
                self.update_timer()
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a positive integer for seconds.")

    def stop_countdown(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.time_entry.config(state=tk.NORMAL)

    def reset_timer(self):
        self.running = False
        self.remaining_time = 0
        self.timer_label.config(text="00:00")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.time_entry.config(state=tk.NORMAL)
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, "60")

    def update_timer(self):
        if self.running and self.remaining_time > 0:
            mins, secs = divmod(self.remaining_time, 60)
            timer_text = '{:02d}:{:02d}'.format(mins, secs)
            self.timer_label.config(text=timer_text)
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        elif self.running and self.remaining_time == 0:
            self.timer_label.config(text="00:00")
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.time_entry.config(state=tk.NORMAL)
            messagebox.showinfo("Time's Up!", "Countdown completed!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()







###########For a simple command-line countdown timer, you can use the following code:#############

#import time

#def countdown(t):
#    while t:
#        mins, secs = divmod(t, 60)
#        timer = '{:02d}:{:02d}'.format(mins,secs)
#        print(timer, end="\r")
#        time.sleep(1)
#        t -= 1

#    print('Timer completed!')

#t = input('Enter the time in seconds: ')

#countdown(int(t))