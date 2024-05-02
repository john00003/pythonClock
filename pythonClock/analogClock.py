import customtkinter as ctk
from tkinter import *
import math


class AnalogClock(Canvas):
    def __init__(self, master):
        super().__init__(master=master)
        super().create_oval(0, 0, 100, 100, fill='white')


    def update(self, time_fields, time_units_per_rotation, updated_time_fields):
        for i in range(0, len(time_fields)):
            if updated_time_fields[i] is None:
                raise Exception('AnalogClock: time not updated properly')
            super().delete(time_fields[i])
            angle = math.pi / 2 - (updated_time_fields[i]) * (2 * math.pi) / time_units_per_rotation[i]
            super().create_line(50, 50, 50 + 20 * math.cos(angle), 50 - 20 * math.sin(angle), width=1,
                                tags=time_fields[i])
