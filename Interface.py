from tkinter import *
from tkinter import ttk
from singlevar import solve_single_variable_equation
from Graph import Graph
from Memory import show_memory
from UnitConverterUI import UnitConverterUI
from Trigonometry import calculate_trig_function
from sympy import symbols, Eq, solve, simplify, tan, sin, cos, log, asin, acos, atan, ln, sympify
from math import *

def button_click(symbol):
    current = display_area.get("1.0", END).strip()
    if symbol == "Del":
        current = current[:-1]
    elif symbol in ["Conv"]:
        current = current
    elif symbol == "Scientific Calculator Mode":
        buttons_specs[0] = ("X", "1", "0", "1", 0.75, 0)
        buttons_specs[17] = ("Del", "1", "0", "1", 0.75, 1)
        buttons_specs[13] = ("Scientific Calculator Mode", "1", "1", "1", 1, 0)
        for i in range(2, 9):
            buttons_specs[i] = (*buttons_specs[i][:5], 1)
        update_button_sizes(None)
    elif symbol == "Normal Mode":
        buttons_specs[0] = ("X", "1", "0", "1", 0.75, 1)
        buttons_specs[17] = ("Del", "3", "0", "1", 1, 1)
        buttons_specs[13] = ("Scientific Calculator Mode", "1", "1", "1", 1, 1)
        for i in range(2, 9):
            buttons_specs[i] = (*buttons_specs[i][:5], 0)
        update_button_sizes(None)
    elif symbol in ["tan", "sin", "cos", "log", "ln"]:
        current += f"{symbol}("
    elif symbol == "Graph":
        graph = Graph()
    elif symbol == "Unit Converter":
        converter = UnitConverterUI()
    elif symbol == "History":
        show_memory(calculations)
    elif symbol == "MC":
        memory_saved[0] = ""
    elif symbol == "MR":
        current += memory_saved[0]
    elif symbol == "MS":
        memory_saved[0] = current
    elif symbol == "AC":
        current = ""
    elif symbol == "^":
        current += "**"
    elif symbol == "√":
        current += "sqrt("
    elif symbol == "deg/rad":
        if is_deg[0] == TRUE:
            is_deg[0] = FALSE
        else:
            is_deg[0] = TRUE
    elif symbol == "π":
        current += "pi"
    elif symbol in ["+", "/", "-", "*", "x²"]:
        if symbol == "*":
            current += "*"
        elif symbol == "x²":
            current += "**2"
        else:
            current += str(symbol)
    elif symbol == "X":
        current += "x"
    elif symbol == "paste":
        current += root.selection_get(selection='CLIPBOARD')
    elif symbol == "Enter" or symbol == "Return":
        if "x" in current:
            try:
                result = solve_single_variable_equation(current)
                calculations.append((current, result))
                current = f"{current} \n{result[0]}"
            except Exception as e:
                current = f"{e}"
            display_area.config(state=NORMAL)
            display_area.delete("1.0", END)
            display_area.insert(END, current)
            display_area.config(state=DISABLED)
        elif symbol in current in ["tan", "sin", "cos", "cos⁻¹", "tan⁻¹", "sin⁻¹"]:
            equation_str = current.replace("tan⁻¹", "atan").replace("cos¹", "acos").replace("sin⁻¹", "asin")
            equation = Eq(sympify(equation_str), 0)
            result = solve(equation)
            calculations.append((current, result))
            current = f"{current} \n{result[0]})"

        else:
            currentcopy = current
            addtomemory = TRUE
            if is_deg[0] == TRUE:
                if current.find("sin") > -1 or current.find("cos") > -1 or current.find("tan") > -1:
                    current = current[:-1]
                    current += "*(pi/180))"
            try:
                current = eval(current)
            except:
                current = "SYNTAX ERROR"
                addtomemory = FALSE
            
            display_area.config(state=NORMAL)
            display_area.delete("1.0", END)
            display_area.insert(END, current)
            display_area.config(state=DISABLED)

            if addtomemory:
                calculations.append(f'{currentcopy} = {current}')
    else:
        current += str(symbol)


    display_area.config(state=NORMAL)
    display_area.delete("1.0", END)
    display_area.insert(END, current)
    display_area.config(state=DISABLED)

def update_button_sizes(event):
    for button in buttons:
        button.destroy()

    create_buttons()


def create_buttons():
    for (text, row, col, colspan, width, visible) in buttons_specs:
        if visible == 1:
            button_text = f" {text} "  # Add spaces for padding between buttons
            button = ttk.Button(frame, text=button_text, command=lambda t=text: button_click(t))
            button.grid(row=int(row), column=int(col), columnspan=int(colspan), pady=5, padx=(5, 10), sticky="nsew")
            buttons.append(button)


# Creates calculator frame / window
root = Tk()
root.title("Calculator")
root.geometry("400x600")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="nsew")

#Displays what the user inputs / the answers
display_area = Text(frame, width=40, height=3, font=("Helvetica", 16), wrap=WORD, state=DISABLED)
display_area.grid(row=0, column=0, columnspan=5, padx=(5, 10), pady=(5, 20))  #Aligns with buttons

#all the buttons
buttons_specs = [
    ("X", "1", "0", "1", 0.75, 1), ("Graph", "1", "4", "1", 0.75, 1), ("sin", "2", "0", "1", 1, 0),
    ("cos", "2", "1", "1", 1, 0), ("tan", "2", "2", "1", 1, 0), ("log", "2", "3", "1", 1, 0), ("ln", "2", "4", "1", 1, 0), ("e", "3", "3", "1", 1, 0), ("Normal Mode", "1", "1", "1", 1, 0),
    ("MC", "3", "1", "1", 1, 1), ("MR", "3", "2", "1", 1, 1), ("MS", "3", "3", "1", 1, 1),
    ("^", "4", "0", "1", 1, 1),("Scientific Calculator Mode", "1", "1", "1", 1, 1), ("Unit Converter", "1", "2", "1", 1, 1), ("History", "1", "3", "1", 1, 1),
    ("x²", "5", "0", "1", 1, 1),("Del", "3", "0", "1", 1, 1), ("(", "4", "2", "1", 1, 1), (")", "4", "3", "1", 1, 1), ("*", "4", "4", "1", 1, 1),
    ("π", "7", "0", "1", 1, 1),("1", "5", "1", "1", 1, 1), ("2", "5", "2", "1", 1, 1), ("3", "5", "3", "1", 1, 1), ("/", "5", "4", "1", 1, 1),
    ("deg/rad", "4", "1", "1", 1, 1),("4", "6", "1", "1", 1, 1), ("5", "6", "2", "1", 1, 1), ("6", "6", "3", "1", 1, 1), ("-", "6", "4", "1", 1, 1),
    ("%", "8", "0", "1", 1, 1),("7", "7", "1", "1", 1, 1), ("8", "7", "2", "1", 1, 1), ("9", "7", "3", "1", 1, 1), ("+", "7", "4", "1", 1, 1),
    ("AC", "3", "4", "1", 1, 1),("0", "8", "1", "2", 1, 1), (".", "8", "3", "1", 1, 1), ("Enter", "8", "4", "1", 1, 1), ("√", "6", "0", "1", 1, 1)
]

buttons = []
calculations = []
memory_saved = [""]
is_deg = [FALSE]
    
# Creates the initial button display on calculator
create_buttons()

# Creates row / column weights so that the buttons expand when the calculator size is changed
for i in range(9):
    frame.grid_rowconfigure(i, weight=1)

for i in range(5):
    frame.grid_columnconfigure(i, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


frame.bind("<Configure>", update_button_sizes)

def button_click_from_key(event):
    valid_keys = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "%", "*", "/", ".", "^", "(", ")", "BackSpace", "Enter", "Return", "x"}

    key = event.char if event.char in valid_keys else event.keysym

    if key == "BackSpace":
        button_click("Del")
    elif key == "x":
        button_click("X")
    elif key in valid_keys:
        button_click(key)
    elif key == "v" and event.state == 4:
        button_click("paste")


root.bind("<Key>", button_click_from_key)

root.mainloop()

