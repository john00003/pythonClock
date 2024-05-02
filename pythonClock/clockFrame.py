import customtkinter as ctk
import digitalClock

#this class will hold a clock, display a title, and hold a settings button for the clock


class ClockFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)

        self.clock_title_label = ctk.CTkLabel(self, text='yippee a clock')
        self.clock_title_label.grid(row=0, column=0)

        self.clock = digitalClock.DigitalClock(self)
        self.clock.grid(row=1, column=0)

