from tkinter import *
from tkinter.ttk import *
from time import time_ns
from time import *
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

lbl = Label(root, font=('calibri', 40, 'bold'),
            background='black',
            foreground='white')
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
