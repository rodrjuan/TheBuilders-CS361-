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
    "Temperature",
    "Mass"
]


class UnitConverterUI:
    def __init__(self):
        # create a converter object instance
        converter = UnitConverter.UnitConverter()

        # create the root window
        root = self.__createRoot()

        # create the top label
        l1 = self.__createLabel(root,"Select Units","20")
        l1.grid(row= 0,column= 0)

        # create Radio Button List
        rb1_select =StringVar(root,"Length")
        rb2_select =StringVar()
        rb3_select =StringVar()
        rb2 = []
        rb3 = []
        rb1 = self.__createRadioButtons(root,rb1_select,OPTIONS, None)
        i = 1
        for rb in rb1:
            rb.grid(row=i,column=0,padx=10)
            i = i+1

        # create the input bar
        l2 = self.__createLabel(root,"Enter a number: ","20")
        l2.grid(row= 1,column= 1)
        e1 = self.__createEntry(root)
        e1.grid(row= 1,column=2, columnspan=2)

        # create "from" list
        l3 = self.__createLabel(root,"From","15")
        l3.grid(row=2, column=1)

        # create "to" list
        l4 = self.__createLabel(root,"To","15")
        l4.grid(row=2, column=3)

        # create a result label
        l5 = self.__createLabel(root,"Result:","15")
        l5.grid(row=1,column=4)

        # create calculate button
        button = self.__createCalculate(root)
        button.grid(row=3,column=5)

    # determine which radio button has been selected
    # def __selection(self,v,root,rb1,rb2):
    #     selected = v.get()
    #     print(selected)
    #     if selected == OPTIONS[0]:
    #         self.__updateToFromButtons(root,v1,v2,rb1,rb2,LENGTHS,self.__selection(v1,root,))
    #     elif selected == OPTIONS[1]:
    #         self.__updateToFromButtons(root,v,rb1,rb2,AREAS)
    #     elif selected == OPTIONS[2]:
    #         self.__updateToFromButtons(root,v,rb1,rb2,VOLUMES)
    #     elif selected == OPTIONS[3]:
    #         self.__updateToFromButtons(root,v,rb1,rb2,TEMPS)
    #     elif selected == OPTIONS[4]:
    #         self.__updateToFromButtons(root,v,rb1,rb2,MASSES)

    # create label function
    def __createLabel(self,root, t, f):
        label = Label(root, text=t, font=f, bg="light grey")

        return label

    # create top level object associated with root window
    def __createRoot(self):
        root = Toplevel(bg="light grey")
        root.geometry("500x200")
        root.title("Unit Converter")
        root.resizable(width=False, height=False)

        return root
    
    # create a radio buttons for choosing units
    def __createRadioButtons(self,root,v,list,cmd):
        buttons = []
        for x in list:
            rb = Radiobutton(root, text=x, variable= v, value= x, indicator=0, width=10,command=cmd)
            buttons.append(rb)

        return buttons

    def __updateToFromButtons(self,root,v1,v2,rb1,rb2,l,cmd1,cmd2):
        # if there are any 
        if len(rb1) > 0:
            self.__deleteRadioButtons(rb1)
            self.__deleteRadioButtons(rb2)

        rb1 = self.__createRadioButtons(root,v1,l,cmd1)
        rb2 = self.__createRadioButtons(root,v2,l,cmd2)

        i = 3
        for rb in rb1:
            rb.grid(row=i,column=1)
        
    def __deleteRadioButtons(self,l):
        for x in l:
            x.grid_forget()
        l.clear()

    def __createEntry(self,root):
        entry = Entry(root)
        return entry
    
    def __createCalculate(self,root):
        button = Button(root, text="Calculate", width=10)
        return button
            



# # create the calculate button
# button = Button(top, text="Calculate", width=10, font=("Helvetica", 12))
# button.grid(row=3,column =1)

# # execute tkinker
# top.mainloop()