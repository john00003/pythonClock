import customtkinter as ctk

class DigitalClock(ctk.CTkLabel):
    def __init__(self, master):
        super().__init__(master=master, text='00:00:00', text_color='#9665eb', fg_color='transparent')
        # digital clock will need a digital clock preferences object
        # self.label = ctk.CTkLabel(master=master, text='00:00:00', fg_color='transparent')
        self.time_fields = ['hour', 'minute', 'second']
        self.updated_time_fields = [None, None, None]
        self.time_field_zero_padding_length = [2, 2, 2]

    def update(self):
        # problem: different digital clocks may have different times to display
        # e.g., hours:min:second or days:hours:min:second:millisecond
        # solution:
        #while user is making time fields in the gui, sort them by ns for each time field added
        #then we can just use them in the order that they will appear in self.time_fields :)
        string = ''
        for i in range(0, len(self.time_fields)):
            string += f'{self.updated_time_fields[i]:0{self.time_fields[i]}d}:'