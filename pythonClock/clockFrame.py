#this class will hold a clock, display a title, and hold a settings button for the clock
#this class will also handle the time being updated, and will provide the clock with the necessary information to update
import customtkinter as ctk
import digitalClock
import analogClock


class ClockFrame(ctk.CTkFrame):
    def __init__(self, master, clock):
        super().__init__(master=master)

        self.time_fields = ['hour', 'minute', 'second']
        self.updated_time_fields = [None, None, None]

        self.clock_title_label = ctk.CTkLabel(self, text='yippee a clock')
        self.clock_title_label.grid(row=0, column=0)

        if clock == 'digital':
            self.clock = digitalClock.DigitalClock(self)
        elif clock == 'analog':
            self.clock = analogClock.AnalogClock(self)
        self.clock.grid(row=1, column=0)

    def update(self):
        self.clock.update(self.time_fields, self.updated_time_fields)
        # clear updated list for next update
        self.updated_time_fields = [None] * len(self.time_fields)
