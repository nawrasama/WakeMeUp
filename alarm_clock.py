import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading
from playsound import playsound  # pip install playsound

# Alarm function 
def alarm(set_alarm_time):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm_time:
            messagebox.showinfo("Alarm", "⏰ Wake up! Time's up!")
            try:
                playsound("alarm.mp3")  # Replace with your file
            except:
                print("Sound file missing or error playing sound.")
            break

#  Button action 
def set_alarm():
    hour = hour_entry.get()
    minute = minute_entry.get()
    second = second_entry.get()

    if not (hour and minute and second):
        messagebox.showerror("Error", "Please enter all time fields.")
        return

    try:
        alarm_time = f"{int(hour):02d}:{int(minute):02d}:{int(second):02d}"
    except ValueError:
        messagebox.showerror("Error", "Invalid time format.")
        return

    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
    # Start alarm in new thread to keep GUI responsive
    t = threading.Thread(target=alarm, args=(alarm_time,))
    t.start()

#  GUI Setup 
root = tk.Tk()
root.title("Python Alarm Clock")
root.geometry("300x250")
root.config(bg="lightblue")

tk.Label(root, text="Set Alarm Time", font=("Helvetica", 14), bg="lightblue").pack(pady=10)

frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=10)

#  Time Input Fields 
hour_entry = tk.Entry(frame, width=5, font=("Helvetica", 18))
hour_entry.grid(row=0, column=0)
tk.Label(frame, text=":", font=("Helvetica", 18), bg="lightblue").grid(row=0, column=1)

minute_entry = tk.Entry(frame, width=5, font=("Helvetica", 18))
minute_entry.grid(row=0, column=2)
tk.Label(frame, text=":", font=("Helvetica", 18), bg="lightblue").grid(row=0, column=3)

second_entry = tk.Entry(frame, width=5, font=("Helvetica", 18))
second_entry.grid(row=0, column=4)

#  Set Alarm Button 
tk.Button(root, text="Set Alarm", command=set_alarm, font=("Helvetica", 14), bg="#34A853", fg="white").pack(pady=20)

root.mainloop()
