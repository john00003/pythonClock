#this class will hold a clock, display a title, and hold a settings button for the clock
#this class will also handle the time being updated, and will provide the clock with the necessary information to update
import customtkinter as ctk
import digitalClock
import analogClock


class ClockFrame(ctk.CTkFrame):
    def __init__(self, master, clock):
        super().__init__(master=master)

        self.time_fields = ['hour', 'minute', 'second']
        # this array holds the units of time that comprise the next greater unit of time
        self.time_units_per = [24, 60, 60]
        self.updated_time_fields = [None, None, None]

        self.clock_title_label = ctk.CTkLabel(self, text='yippee a clock')
        self.clock_title_label.grid(row=0, column=0)

        # TODO: add a time_managers field that keeps track of the time_managers that interact with this clock
        # TODO: when this clock is deleted or edited, we can easily remove this clock from any time managers

        if clock == 'digital':
            self.clock = digitalClock.DigitalClock(self)
        elif clock == 'analog':
            self.clock = analogClock.AnalogClock(self)
        self.clock.grid(row=1, column=0)

    def update(self):
        self.clock.update(self.time_fields, self.time_units_per, self.updated_time_fields)
        # clear updated list for next update
        self.updated_time_fields = [None] * len(self.time_fields)
