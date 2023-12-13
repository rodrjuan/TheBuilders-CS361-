# import dependencies
from tkinter import *
import UnitConverter

# drop down menu options
LENGTHS = [
    "Tm",
    "Gm",
    "Mm",
    "km",
    "m",
    "dam",
    "dm",
    "cm",
    "mm",
    "mum",
    "nm",
    "pm"
]

# create object
root = Tk()

root.geometry( "200x200" )

# Change the label text
def show():
    label.convig( text = clicked.get())

# data type of menu text
clicked = StringVar()

# initial menu text
clicked.set("m")

# create dropdown menu
drop = OptionMenu( root, clicked, *LENGTHS)
drop.pack()

# create button, change label text
button = Button( root, text = "click me", command = show).pack()

# create label
label = Label(root, text = "")
label.pack()

# execute tkinker
root.mainloop()