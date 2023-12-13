# import dependencies
from tkinter import *
from tkinter import ttk
import UnitConverter

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
    "Mass",
    "SELECT"
]


# def openConverter():
# create a converter object instance
converter = UnitConverter.UnitConverter()


# create top level object associated with root window
top = Toplevel()
top.geometry("500x200")
top.title("Unit Converter")

val = ""

# create a description of the window
des = Label(top, text="Convert from one unit to another", font=("Helvetica", 12))
des.grid(row=0)

# create a Entry box for user input
Label(top, text="Enter a number:", font=("Helvetica", 12)).grid(row=1,column=0)
entry = Entry(top)
entry.grid(row=1,column=1)

def get(x):
    c = x.get()
    return c
# create 5 buttons to show functionality
b1 = Button(top, text="Inches to Meters",comme)
b1.grid(row=3,column=1)

b2 = Button(top, text="Miles Squared to Kilometers Squared")
b2.grid(row=4,column=1)

b3 = Button(top, text="Millimeters Cubed to Kilometers Cubed")
b3.grid(row=5,column=1)

b4 = Button(top, text="Fehrenheit to Kelvin")
b4.grid(row=6,column=1)

# # create a dropdown menu for choosing units
# units = Menubutton(top, text = "SELECT")
# units.grid(row=2,column=0)

# units.menu = Menu(units, tearoff=0)
# units["menu"] = units.menu
# for x in OPTIONS:
#     units.menu.add_checkbutton(label=x)
# units.grid()

# # logic to change label when user selects an option
# def selected(menu,text):
#     menu.option_add("text",text)


# # create a dropdown menu for choosing input unit
# input = Menubutton(top, text = "FROM")
# input.grid(row=2,column=1)

# input.menu = Menu(input, tearoff=0)
# input["menu"] = input.menu
# for x in LENGTHS:
#     input.menu.add_checkbutton(label=x)
# input.grid()

# # create a dropdown menu for choosing output unit
# output = Menubutton(top, text = "TO")
# output.grid(row=2,column=2)

# output.menu = Menu(output, tearoff=0)
# output["menu"] = output.menu
# for x in LENGTHS:
#     output.menu.add_checkbutton(label=x)
# output.grid()

# # create the calculate button
# button = Button(top, text="Calculate", width=10, font=("Helvetica", 12))
# button.grid(row=3,column =1)

# execute tkinker
top.mainloop()