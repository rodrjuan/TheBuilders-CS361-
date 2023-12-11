# import dependencies
from tkinter import *
from tkinter import ttk

# CONSTANTS
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
    "pm",
    "in",
    "yd",
    "mi"
]

AREAS = [
    "Tm sq",
    "Gm sq",
    "Mm sq",
    "km sq",
    "m sq",
    "dam sq",
    "dm sq",
    "cm sq",
    "mm sq",
    "mum sq",
    "nm sq",
    "pm sq",
    "in sq",
    "yd sq",
    "mi sq"
]

VOLUMES = [
    "Tm cb",
    "Gm cb",
    "Mm cb",
    "km cb",
    "m cb",
    "dam cb",
    "dm cb",
    "cm cb",
    "mm cb",
    "mum cb",
    "nm cb",
    "pm cb",
    "in cb",
    "yd cb",
    "mi cb"
]

TEMPS = [
    "Kelvin",
    "Celcius",
    "Fehrinheit"
]

MASSES = [
    "kg",
    "g",
    "mg",
    "lb",
    "oz",
    "ton",

]

OPTIONS = [
    "Length",
    "Area",
    "Volume",
    "Tempurature",
    "Mass"
]


# create test root object, initialize some values
root = Tk()

root.geometry( "200x300" )
root.title("Main")

# label to identify window
l = Label(root, text = "This is the test root window")



# create top level object associated with root window
top = Toplevel(root)
top.geometry("180x100")
top.title("Unit Converter")

l2 = Label(top, text = "Select units to convert.")


# data type of menu text
clicked = StringVar()

# initial menu text
clicked.set("m")

# create dropdown menu
drop = OptionMenu( top, clicked, *LENGTHS)
drop.pack()


# execute tkinker
root.mainloop()