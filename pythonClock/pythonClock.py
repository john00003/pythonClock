from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from time import time_ns
from time import *
import customtkinter as ctk
import math

# creating tkinter window
root = Tk()
root.title('Clock')

# can do template method for analog and digital clock?
# can do command for addition/deletion (or more generally, customization) of hands? easy to undo and redo?
def time():
    # to display milliseconds, we get the seconds since the epoch rounded down to the nearest second
    # we convert those seconds into ns
    # then we get the time in nanoseconds, subtracting the previous value
    # then we convert that difference to milliseconds
    # check if it is over 1000 (if we have moved to next second), subtracting 1000 if so
    # then we display
    closest_seconds = time_ns() // 1000000000
    closest_seconds = closest_seconds * 1000000000
    ms_since_second_start = (time_ns() - closest_seconds) // 1000000
    if ms_since_second_start > 1000:
        ms_since_second_start -= 1000

    ns_time = time_ns()
    #TODO: move this to a function and reduce # of operations per function call
    string = f'{(ns_time % (1000000000*3600*24)) // (1000000000*3600):02d}:{(ns_time % (1000000000*60*60)) // (1000000000*60):02d}:{(ns_time % (1000000000*60)) // (1000000000):02d}:{ms_since_second_start:03d}'

    for hand in hands:
        update_hands(hand, ns_time)

    lbl.config(text=string)
    lbl.after(1, time)


def update_hands(hand, current_time):
    # delete previous hand
    canvas.delete(hand[0])
    # calculate angle to draw hand at
    angle = math.pi / 2 - ((current_time % hand[2]) // hand[1]) * (hand[1] * 2 * math.pi)/hand[2]
    canvas.create_line(50, 50, 50 + 20 * math.cos(angle), 50 - 20 * math.sin(angle), width=1, tags=hand[0])

def init_settings_button(label):
    label.settings_button = ctk.CTkButton(label, text='Settings', fg_color='red', anchor='se', bg_color='transparent')
    label.settings_button.pack()
    label.settings_button.place(relx=1, rely=1, anchor='se')


    # label.settings_button = ttk.Button(label, text='Settings')
    #
    # label.settings_button.place(relx=1.0, rely=1.0, x=-2, y=-2, anchor="se")

lbl = Label(root, font=('calibri', 40, 'bold'),
            background='black',
            foreground='white')
# style = Style().configure('TButton', background='red', activebackground='black', foreground='green')
init_settings_button(lbl)
canvas = Canvas(root)
canvas.create_oval(0, 0, 100, 100, fill='white')


lbl.grid(column=0, row=0)
canvas.grid(column=1, row=0)
# hands are represented a tuples of the format (name, ns per tick, ns per circle)
# TODO: maybe turn to struct
hands = [('seconds', 1000000000, 1000000000*60), ('minutes', 1000000000*60, 1000000000*60*60), ('hours', 1000000000*60*60, 1000000000*60*60*12)]

# Placing clock at the centre
# of the tkinter window
# lbl.pack(anchor='center')
time()

mainloop()

#problem
#we are going to have lots of different clock objects at the same time
#some will have different hands: hands for months, hands for days, hands for hours, etc.
#lets say we have calculated the current hour of the day, and we want to provide this to multiple different clocks
#how to do we provide it?

#let our app (main loop) maintain an array of classes: TimeManagers
#each struct consists of four fields: (tag, ns in one unit of time, ns in one full rotation, list of clocks using this unit of time)
#when a new clock is added, we loop through the list of structs to see if we are already keeping track of this unit of time
    #if so, add clock to the list
    #else, make a new struct with clock in the list
#when main loop goes to provide each clock with the time in ns, it will instead provide TimeManager with the time in ns
#TimeManager will loop through each clock in it's array, and provide it with the corresponding details
#clock will have more than one TimeManager interacting with it, one for each of it's fields (e.g., second, min, hour)

#then, once main loop has looped through each TimeManager, all clocks are ready to be updated
#main loop can update all of it's clocks
#each clock should have all of it's required fields updated
    #if not, throw error
#after displaying updated time, each clock will reset each of it's fields to indicate that it must be updated in next time step

