from tkinter import *
from tkinter import ttk
from singlevar import solve_single_variable_equation
from Graph import Graph
from Memory import show_memory

def button_click(symbol):
    current = display_area.get("1.0", END).strip()
    if symbol == "Del":
        current = current[:-1]
    elif symbol in ["SC mode", "Conv"]:
        current = current
    elif symbol == "Graph":
        graph = Graph()
    elif symbol == "Memory":
        show_memory(calculations)
    elif symbol == "AC":
        current = ""
    elif symbol == "^":
        current += "**"
    elif symbol == "√":
        current += "sqrt("
    elif symbol == "(-)":
        current += " -"
    elif symbol == "π":
        current += "pi"
    elif symbol in ["+", "/", "-", "*", "x²"]:
        if symbol == "*":
            current += " * "
        elif symbol == "x²":
            current += "**2"
        else:
            current += " " + str(symbol) + " "
    elif symbol == "X":
        current += "x"
    elif symbol == "Enter" or symbol == "Return":
        if "x" in current:
            result = solve_single_variable_equation(current)
            calculations.append((current, result))
            current = f"{current} \n{result[0]}"
            display_area.config(state=NORMAL)
            display_area.delete("1.0", END)
            display_area.insert(END, current)
            display_area.config(state=DISABLED)
        else:
            currentcopy = current
            current = eval(current)
            display_area.config(state=NORMAL)
            display_area.delete("1.0", END)
            display_area.insert(END, current)
            display_area.config(state=DISABLED)
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
    for (text, row, col, colspan, width) in buttons_specs:
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
    ("X", "1", "0", "1", 0.75), ("Graph", "1", "4", "1", 0.75),
    ("^", "4", "0", "1", 1),("SC mode", "1", "1", "1", 1), ("Conv", "1", "2", "1", 1), ("Memory", "1", "3", "1", 1),
    ("x²", "5", "0", "1", 1),("Del", "3", "0", "1", 1), ("(", "4", "2", "1", 1), (")", "4", "3", "1", 1), ("*", "4", "4", "1", 1),
    ("π", "7", "0", "1", 1),("1", "5", "1", "1", 1), ("2", "5", "2", "1", 1), ("3", "5", "3", "1", 1), ("/", "5", "4", "1", 1),
    ("(-)", "4", "1", "1", 1),("4", "6", "1", "1", 1), ("5", "6", "2", "1", 1), ("6", "6", "3", "1", 1), ("-", "6", "4", "1", 1),
    ("%", "8", "0", "1", 1),("7", "7", "1", "1", 1), ("8", "7", "2", "1", 1), ("9", "7", "3", "1", 1), ("+", "7", "4", "1", 1),
    ("AC", "3", "4", "1", 1),("0", "8", "1", "2", 1), (".", "8", "3", "1", 1), ("Enter", "8", "4", "1", 1), ("√", "6", "0", "1", 1)
]

buttons = []
calculations = []

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


root.bind("<Key>", button_click_from_key)

root.mainloop()

