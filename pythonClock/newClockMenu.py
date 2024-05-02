from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from time import time_ns
from time import *
import customtkinter as ctk
import math


class NewClockMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, bg_color='#9665eb')

        self.title_label = ctk.CTkLabel(self, text='pyClock', text_color='#f7c5fb')
        self.title_label.grid(row=0, column=0)
        self.new_analog_clock_buton = ctk.CTkButton(self, text='New Analog Clock', fg_color='#f7c5fb', text_color='#9665eb')
        self.new_analog_clock_buton.grid(row=1, column=0)
        self.new_digital_clock_button = ctk.CTkButton(self, text='New Digital Clock', fg_color='#f7c5fb', text_color='#9665eb')
        self.new_digital_clock_button.grid(row=2, column=0)

