import tkinter
from tkinter import *

from time import strftime

clock = Tk()
clock.geometry("800x175")
clock.title("Clock")

def time():
    string = strftime("%I:%M:%S %p")
    label.config(text = string)
    label.after(1000, time)

label = Label(clock, font = "ds-digital 100", background = "yellow", foreground = "green")
label.place(x=10,y=5)

time()

mainloop()