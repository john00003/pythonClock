import customtkinter as ctk

import clockFrame
import newClockMenu
import analogClock
import digitalClock
import timeManager

from time import *
from time import sleep


class PythonClockApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x1000')
        # self.grid_rowconfigure(0, weight=1)  # configure grid system
        # self.grid_columnconfigure(0, weight=1)
        self.time_managers = []
        self.clocks = []

        self.menu = newClockMenu.NewClockMenu(master=self)
        clock1 = clockFrame.ClockFrame(master=self, clock='analog')
        clock2 = clockFrame.ClockFrame(master=self, clock='digital')

        self.add_clock(clock1, [(1000000000 * 3600), (1000000000 * 60), (1000000000)],
                       [(1000000000 * 3600 * 24), (1000000000 * 60 * 60), (1000000000 * 60)])
        self.add_clock(clock2, [(1000000000 * 3600), (1000000000 * 60), (1000000000)],
                       [(1000000000 * 3600 * 24), (1000000000 * 60 * 60), (1000000000 * 60)])
        # self.clock1 = clockFrame.ClockFrame(master=self, clock='analog')
        # self.clock2 = clockFrame.ClockFrame(master=self, clock='digital')

        self.menu.grid(row=0, column=0)
        self.clocks[0].grid(row=0, column=1)
        self.clocks[1].grid(row=0, column=2)

    def time(self):
        ns_time = time_ns()
        for manager in self.time_managers:
            manager.update(ns_time)
        for clock in self.clocks:
            clock.update()
        super().after(100, self.time)

    def add_clock(self, clock, ns_per_units, ns_per_cycles):
        i = 0
        for field in clock.time_fields:
            index = -1
            try:
                # if this time manager already exists, we append our clock to its clocks list
                index = self.time_managers.index(field)
                self.time_managers[index].clocks.append(clock)
            except ValueError:
                # add a new time manager
                # TODO: sort time managers?
                self.time_managers.append(timeManager.TimeManager(field, ns_per_units[i], ns_per_cycles[i], [clock]))
            i += 1
        self.clocks.append(clock)


app = PythonClockApp()
app.time()
app.mainloop()
