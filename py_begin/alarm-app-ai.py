# imports and global variables

import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

alarm_time = None
clock_job = None  # id of the scheduled `after` call, needed to cancel it on close

window = tk.Tk()
window.title('alarm app')
window.resizable(width=False, height=False)
window.geometry('500x400')


# function for getting current time

def get_current_time():
    global clock_job
    current_time = datetime.now()
    time_label.configure(text=current_time.strftime('%H:%M:%S'))
    compare_alarm_with_current_time(current_time)
    clock_job = window.after(1000, get_current_time)


# function set alarm timer

def set_alarm():
    global alarm_time
    try:
        hour = int(hour_alarm_entry.get())
        minute = int(minute_alarm_entry.get())
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            raise ValueError
    except ValueError:
        messagebox.showerror('خطا', 'ساعت (۰ تا ۲۳) و دقیقه (۰ تا ۵۹) را صحیح وارد کنید')
        return

    current_time = datetime.now()
    alarm_time = current_time.replace(hour=hour, minute=minute, second=0, microsecond=0)

    # اگر زمان وارد شده از الان گذشته باشد، آلارم برای فردا تنظیم می‌شود
    if alarm_time <= current_time:
        alarm_time += timedelta(days=1)

    latest_alarm_label.configure(text=alarm_time.strftime('%H:%M:%S'))
    # print('alarm has been set', hour_alarm_entry.get(), minute_alarm_entry.get())


# function for comparing time with alarm

def compare_alarm_with_current_time(current_time):
    global alarm_time
    if alarm_time is not None and current_time >= alarm_time:
        messagebox.showinfo('showinfo', 'wake up babe')
        latest_alarm_label.configure(text='no alarm has been set')
        alarm_time = None


# function for closing the app cleanly (fixes the "won't close" issue)

def on_closing():
    global clock_job
    if clock_job is not None:
        window.after_cancel(clock_job)
    window.destroy()


# ui design

# text time

time_label = tk.Label(window, text='12:30:30', font=('Titr', 32))
time_label.pack()

# text input hour

tk.Label(window, text='Hour').pack()
hour_alarm_entry = tk.Entry(window)
hour_alarm_entry.pack()

# text input minute

tk.Label(window, text='Minute').pack()
minute_alarm_entry = tk.Entry(window)
minute_alarm_entry.pack()

# button set alarm

tk.Button(window, text='Set Alarm', command=set_alarm).pack()

# showing last alarm

latest_alarm_label = tk.Label(window, text='no alarm has been set')
latest_alarm_label.pack()

# make sure clicking the X button runs our cleanup instead of just destroying the window

window.protocol('WM_DELETE_WINDOW', on_closing)

# run application
get_current_time()
window.mainloop()