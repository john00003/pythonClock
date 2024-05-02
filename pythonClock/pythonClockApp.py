import customtkinter as ctk

import clockFrame
import newClockMenu
import analogClock
import digitalClock

from time import *


class PythonClockApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x1000')
        # self.grid_rowconfigure(0, weight=1)  # configure grid system
        # self.grid_columnconfigure(0, weight=1)

        self.menu = newClockMenu.NewClockMenu(master=self)
        self.clock1 = clockFrame.ClockFrame(master=self, clock='analog')
        self.clock2 = clockFrame.ClockFrame(master=self, clock='digital')

        self.menu.grid(row=0, column=0)
        self.clock1.grid(row=0, column=1)
        self.clock2.grid(row=0, column=2)

    def time(self):
        ns_time = time_ns()
        for manager in self.time_managers:
            manager.update(ns_time)
        for clock in self.clocks:
            clock.update()


app = PythonClockApp()
app.mainloop()
