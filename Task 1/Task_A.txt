# -*- coding: utf-8 -*-
"""
Created on Tue May 12 05:07:19 2023

@author: Vinothini S
"""

import tkinter as tk
from datetime import datetime, timedelta

class HandWatch(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.mode = 0
        self.time_label = tk.Label(self, font=('Helvetica', 48))
        self.time_label.pack(padx=20, pady=20)
        self.mode_button = tk.Button(self, text='Mode', command=self.toggle_mode)
        self.mode_button.pack(side='left', padx=20, pady=20)
        self.increase_button = tk.Button(self, text='+1 hour', command=self.increase_time)
        self.increase_button.pack(side='left', padx=20, pady=20)
        self.light_button = tk.Button(self, text='Light', command=self.toggle_light)
        self.light_button.pack(side='right', padx=20, pady=20)
        self.pack()
        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.after(1000, self.update_time)

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
            new_time = datetime.now() + timedelta(hours=1)
        elif self.mode == 1:
            new_time = datetime.now() + timedelta(minutes=1)
        else:
            return
        self.time_label.config(text=new_time.strftime('%H:%M:%S'))

    def toggle_light(self):
        bg_color = self.cget('bg')
        if bg_color == 'white':
            self.configure(bg='black')
            self.time_label.configure(fg='white')
        else:
            self.configure(bg='white')
            self.time_label.configure(fg='black')

root = tk.Tk()
root.title('Hand Watch')
root.geometry('400x200')
watch = HandWatch(master=root)
watch.mainloop()
