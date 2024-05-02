import customtkinter as ctk

import clockFrame
import newClockMenu


class pythonClockApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x1000')
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.menu = newClockMenu.NewClockMenu(master=self)
        self.clock = clockFrame.ClockFrame(master=self)

        self.menu.grid(row=0, column=0)
        self.clock.grid(row=0, column=1)


app = pythonClockApp()
app.mainloop()
