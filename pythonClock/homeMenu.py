from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from time import time_ns
from time import *
import customtkinter as ctk
import newClockWindow
import math

class HomeMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, bg_color='#9665eb')

        self.title_label = ctk.CTkLabel(self, text='pyClock', text_color='#f7c5fb')
        self.title_label.grid(row=0, column=0)
        self.new_clock_button = ctk.CTkButton(self, text='New Clock', fg_color='#f7c5fb', text_color='#9665eb', command=self.new_clock)
        self.new_clock_button.grid(row=1, column=0)

    def new_clock(self):
        root = newClockWindow.NewClockWindow()
        root.title('New Clock')
        root.mainloop()
