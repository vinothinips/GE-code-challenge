# -*- coding: utf-8 -*-
"""
Created on Tue May 16 10:47:26 2023

@author: Vinothini S
"""

import tkinter as tk
from datetime import datetime, timedelta
import pytz
import tkinter.simpledialog as simpledialog

class Clock(tk.Frame):
    def __init__(self, master=None, timezone=None):
        super().__init__(master)
        self.timezone = timezone
        self.use_24h_format = True
        self.label = tk.Label(self, font=('Helvetica', 32))
        self.label.pack()
        
        self.mode = 0
        self.time_label = tk.Label(self, font=('Helvetica', 48))
        self.time_label.pack(padx=20, pady=20)
        self.mode_button = tk.Button(self, text='Mode', command=self.toggle_mode)
        self.mode_button.pack(side='left', padx=20, pady=20)
        self.increase_button = tk.Button(self, text='+1 hour', command=self.increase_time)
        self.increase_button.pack(side='left', padx=20, pady=20)
        self.reset_button = tk.Button(self, text='Reset', command=self.reset_time)
        self.reset_button.pack(side='left', padx=20, pady=20)
        self.pack(side='left')
        
        
        self.update_time()

    def update_time(self):
        tz = pytz.timezone(self.timezone)
        current_time = datetime.now(tz)
        if self.use_24h_format:
            time_str = current_time.strftime('%H:%M:%S')
        else:
            time_str = current_time.strftime('%I:%M:%S %p')
        self.time_label.config(text=time_str)
        self.after(1000, self.update_time)

    def toggle_format(self):
        self.use_24h_format = not self.use_24h_format
        self.update_time()
        
    def toggle_mode(self):
        self.mode = (self.mode + 1) % 3
        if self.mode == 0:
            self.increase_button.config(text='+1 hour')
        elif self.mode == 1:
            self.increase_button.config(text='+1 min')
        else:
            self.increase_button.config(state='disabled')
       
    def increase_time(self):
        if self.mode == 0:
            tz = pytz.timezone(self.timezone)
            new_time = datetime.now(tz) + timedelta(hours=1)
        elif self.mode == 1:
            tz = pytz.timezone(self.timezone)
            new_time = datetime.now(tz) + timedelta(minutes=1)
        else:
            return
        self.time_label.config(text=new_time.strftime('%H:%M:%S'))

    def reset_time(self):
        tz = pytz.timezone(self.timezone)
        current_time = datetime.now(tz).strftime('%H:%M:%S')
        self.time_label.config(text=current_time)

class MultiClock(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.clocks = []
        self.clock_frame = tk.Frame(self)
        self.clock_frame.pack(side=tk.LEFT)
        self.create_clock_button = tk.Button(self, text='Create new clock', command=self.create_clock)
        self.create_clock_button.pack(padx=20, pady=20, side=tk.TOP)
        self.format_button = tk.Button(self, text='Toggle Format', command=self.toggle_format)
        self.format_button.pack(side=tk.TOP)
        self.reset_all_button = tk.Button(self, text='Reset all clocks', command=self.reset_all)
        self.reset_all_button.pack(padx=20, pady=20)
        self.pack()

    def create_clock(self):
        timezone = tk.simpledialog.askstring('New Clock', 'Enter timezone (ex: Europe/Paris):')
        if timezone:
            clock = Clock(self.clock_frame, timezone)
            clock.pack(side=tk.LEFT)
            self.clocks.append(clock)

    def reset_all(self):
        for clock in self.clocks:
            clock.destroy()
        self.clocks.clear()

    def toggle_format(self):
        for clock in self.clocks:
            clock.toggle_format()
            
root = tk.Tk()
root.title('Multi-Clock Watch')
root.geometry('800x300')
multi_clock = MultiClock(master=root)
multi_clock.pack()
reset_button = tk.Button(root, text='Reset All', command=multi_clock.reset_all)
reset_button.pack()
multi_clock.mainloop()
