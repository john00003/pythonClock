import customtkinter as ctk

# maybe rename? this could be reused as any command-executing window
# it can be used for modifying existing clocks, modifying the grid layout, etc.
class NewClockWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.window_frame = None

        self.cancel_button = ctk.CTkButton(master=self, text='Cancel', command=self.cancel, fg_color='#f7c5fb', text_color='#9665eb', anchor=ctk.CENTER)
        self.cancel_button.grid(row=0, column=0)
        self.confirm_button = ctk.CTkButton(master=self, text='Confirm', command=self.confirm, fg_color='#f7c5fb', text_color='#9665eb', anchor=ctk.CENTER)
        self.confirm_button.grid(row=0, column=1)

    def change_state(self, state):
        # delete all children
        for child in self.window_frame.winfo_children():
            child.destroy()

        self.window_frame.destroy()
        # TODO: change from state
        self.window_frame = state(master=self)

    def confirm(self):
        self.window_frame.confirm()
        for child in self.window_frame.winfo_children():
            child.destroy()
        self.window_frame.destroy()
        self.destroy()

    def cancel(self):
        for child in self.window_frame.winfo_children():
            child.destroy()
        self.window_frame.destroy()
        self.destroy()

