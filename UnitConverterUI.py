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




# create top level object associated with root window
top = Toplevel(root)
top.geometry("500x600")
top.title("Unit Converter")

# create a description of the window
des = Label(top, text="Convert from one unit to another", font=("Helvetica", 12))
des.grid(row=0)

# create a dropdown menu for choosing units
units = Menubutton(top, text = "SELECT")
units.grid(row=1,column=0)

for unit in UNITS:
    

# create a Entry box for user input
Label(top, text="Enter a number:", font=("Helvetica", 12)).grid(row=1,column=1)
entry = Entry(top)
entry.grid(row=1,column=2)

# create a dropdown menu for choosing input unit

# create a dropdown menu for choosing output unit

# create the calculate button
button = Button(top, text="Calculate", width=10, font=("Helvetica", 12))
button.grid(row=2)

# execute tkinker
root.mainloop()