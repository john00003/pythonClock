import customtkinter as ctk


class DigitalClock(ctk.CTkLabel):
    def __init__(self, master):
        super().__init__(master=master, text='00:00:00', text_color='#9665eb', fg_color='transparent')
        self.time_field_zero_padding_length = [2, 2, 2]

    def update(self, time_fields, time_units_per_rotation, updated_time_fields):
        # problem: different digital clocks may have different times to display
        # e.g., hours:min:second or days:hours:min:second:millisecond
        # solution:
        # while user is making time fields in the gui, sort them by ns for each time field added
        # then we can just use them in the order that they will appear in self.time_fields :)
        string = ''
        for i in range(0, len(time_fields)):
            if updated_time_fields[i] is None:
                raise Exception('AnalogClock: time not updated properly')
            # we modulo in case of not military time i.e. 23 goes to 11
            string += f'{(updated_time_fields[i] % time_units_per_rotation[i]):0{self.time_field_zero_padding_length[i]}d}:'
        super().configure(text=string)
