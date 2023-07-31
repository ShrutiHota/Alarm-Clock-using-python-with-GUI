import tkinter as tk
import datetime
import winsound

class AlarmClockGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Alarm Clock")
        
        self.time_label = tk.Label(self.root, font=("Arial", 100), text="")
        self.time_label.pack(pady=20)
        
        self.set_button = tk.Button(self.root, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack(pady=10)
        
        self.stop_button = tk.Button(self.root, text="Stop Alarm", command=self.stop_alarm, state=tk.DISABLED)
        self.stop_button.pack(pady=10)
        
        self.alarm_time = None
        self.alarm_set = False
        
        self.update_time()
    
    def update_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        
        if self.alarm_set and datetime.datetime.now() >= self.alarm_time:
            self.stop_alarm()
            self.play_alarm_sound()
        
        self.root.after(1000, self.update_time)
    
    def set_alarm(self):
        self.alarm_time = datetime.datetime.now() + datetime.timedelta(minutes=1)  # Set alarm 1 minute from current time
        self.alarm_set = True
        self.set_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
    
    def stop_alarm(self):
        self.alarm_set = False
        self.set_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
    
    def play_alarm_sound(self):
        # Play a system beep sound 5 times
        for _ in range(5):
            winsound.Beep(1000, 2000)  # Frequency: 1000Hz, Duration: 2 seconds
    
    def run(self):
        self.root.mainloop()

# Create an instance of the AlarmClockGUI class and run the GUI
alarm_clock = AlarmClockGUI()
alarm_clock.run()
