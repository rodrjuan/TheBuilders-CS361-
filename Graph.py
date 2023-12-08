# Many parts of this graphing calculator are attributed to this open-source implentation https://github.com/bkthomps/GraphingCalculator
# This version however does have many changes and additions, such as the class layout, code documentation, keyboard shortcuts
# and an interface that matches with the rest of our program.

from tkinter import *
from tkinter import ttk
from math import *

class Graph:
    def __init__(self):
        
        # create the toplevel object that holds everything
        self.graph_root = Toplevel()
        self.graph_root.title("2D Graphing")
        self.graph_root.geometry("400x600")
        self.graph_root.resizable(width=False, height=False)

        # definitions of some member attributes
        self.graph_coord_size = 10
        self.buttons = []
        self.user_input = ""
        self.asymptote = 2.0
        self.computation_distance = 0.001 # acts as graph resolution, decreasing will slow performance but may increase graph fidelity (0.001 recommended)
        self.colors = ["red", "blue", "green3", "gold"]
        self.color_idx = 0

        # create frame that will hold all the widgets
        self.frame = Frame(self.graph_root, padx=10, pady=10)
        self.frame.grid(row=0, column=0, sticky="nsew")

        # create buttons info
        self.buttons_specs = [
        ("EXIT", "1", "0", "1"), ("log", "1", "1", "1"), ("ln", "1", "2", "1"),
        ("e", "1", "3", "1"), ("Color", "1", "4", "1"),
        ("^", "4", "0", "1"),("sin", "3", "1", "1"), ("cos", "3", "2", "1"), ("tan", "3", "3", "1"),
        ("x²", "5", "0", "1"),("Del", "3", "0", "1"), ("(", "4", "2", "1"), (")", "4", "3", "1"), ("*", "4", "4", "1"),
        ("x", "7", "0", "1"),("1", "5", "1", "1"), ("2", "5", "2", "1"), ("3", "5", "3", "1"), ("/", "5", "4", "1"),
        ("pow(x)", "4", "1", "1"),("4", "6", "1", "1"), ("5", "6", "2", "1"), ("6", "6", "3", "1"), ("-", "6", "4", "1"),
        ("", "8", "0", "1"),("7", "7", "1", "1"), ("8", "7", "2", "1"), ("9", "7", "3", "1"), ("+", "7", "4", "1"),
        ("AC", "3", "4", "1"),("0", "8", "1", "2"), (".", "8", "3", "1"), ("Enter", "8", "4", "1"), ("π", "6", "0", "1")
        ]

        # create all the widgets
        self.canvas = Canvas(self.frame)
        
        self.display_area = self.create_display_area()
        self.create_buttons()

        # make the widgets evenly fill in the empty space
        for i in range(9):
            self.frame.grid_rowconfigure(i, weight=1)

        for i in range(5):
            self.frame.grid_columnconfigure(i, weight=1)

            self.graph_root.grid_rowconfigure(0, weight=1)
            self.graph_root.grid_columnconfigure(0, weight=1)

        self.draw_grid_lines()
        self.canvas.grid(row=0, column=0, columnspan=5)

        # set up key bindings
        self.graph_root.bind("<Key>", self.button_click_from_key)

    def button_click(self, symbol):
        if symbol in "0123456789":
            self.append_number(symbol)
        elif symbol in "+-*/).":
            self.append_operator(symbol)
        elif symbol in ["sin", "cos", "tan", "log", "ln", "π", "e", "^", "x", "(", "x²", "pow(x)"]:
            self.append_advanced(symbol)
        elif symbol == "AC":
            self.clear_input()
        elif symbol == "Del":
            self.delete()
        elif symbol == "Enter" or symbol == "Return":
            self.draw_graph()
        elif symbol == "Color":
            self.change_color()
        elif symbol == "EXIT":
            self.graph_root.destroy()

    def change_color(self):
        self.color_idx += 1
        if self.color_idx >= 4:
            self.color_idx = 0
        self.draw_graph()

    def create_display_area(self):
        display_area = Text(self.frame, width=42, height=1, font=("Helvetica", 12))
        display_area.insert("1.0", f"f(x) = {self.user_input}")
        display_area.grid(row=1, column=0, columnspan=5)
        return display_area

    def update_display_area(self):
        self.display_area = Text(self.frame, width=42, height=1, font=("Helvetica", 12))
        self.display_area.insert("1.0", f"f(x) = {self.user_input}")
        self.display_area.grid(row=1, column=0, columnspan=5)  

    def create_buttons(self):
        for (text, row, col, colspan) in self.buttons_specs:
            button = ttk.Button(self.frame, text=text, command=lambda t=text: self.button_click(t))
            button.grid(row=int(row) + 1, column=int(col), columnspan=int(colspan), sticky="nsew")
            self.buttons.append(button)

    def convert_coord_to_canvas_units(self, x_coord, y_coord):
        converted_coord = [0, 0]
        x_mul = int(self.canvas["width"]) / (self.graph_coord_size * 2)
        y_mul = (int(self.canvas["height"]) / (self.graph_coord_size * -2))
        converted_coord[0] = (x_coord + self.graph_coord_size) * x_mul
        converted_coord[1] = (y_coord + self.graph_coord_size) * y_mul + int(self.canvas["height"])
        return converted_coord

    def draw_grid_lines(self):

        # draw x axis
        coord_1 = self.convert_coord_to_canvas_units(self.graph_coord_size * -1, 0)
        coord_2 = self.convert_coord_to_canvas_units(self.graph_coord_size, 0)
        self.canvas.create_line(coord_1[0], coord_1[1], coord_2[0], coord_2[1], fill="black")

        # draw y axis
        coord_1 = self.convert_coord_to_canvas_units(0, self.graph_coord_size)
        coord_2 = self.convert_coord_to_canvas_units(0, self.graph_coord_size * -1)
        self.canvas.create_line(coord_1[0], coord_1[1], coord_2[0], coord_2[1], fill="black")

    def draw_line(self, x1, y1, x2, y2):

        # convert the calculated coords to the coords of the tkinter canvas
        from_coord = self.convert_coord_to_canvas_units(x1, y1)
        to_coord = self.convert_coord_to_canvas_units(x2, y2)

        # if the difference in y-values is greater than a certain threshold, this means there is an asymptote at this specific x value 
        # so set the coords equal to each other to draw a blank line
        if y2 - y1 > self.graph_coord_size * self.asymptote or y1 - y2 > self.graph_coord_size * self.asymptote:
            from_coord = to_coord

        self.canvas.create_line(from_coord[0], from_coord[1], to_coord[0], to_coord[1], fill=self.colors[self.color_idx], width=2)

    def draw_graph(self):
        # reset the canvas
        self.canvas.delete("all")
        self.draw_grid_lines()

        x = self.graph_coord_size * -1
        y = 0.0
        y_previous = 0.0    # after graphing, store the to-value in here to make it the from-value of the next coord

        # loop through all x values that are in frame
        while x <= self.graph_coord_size:
            try:
                # check if the user input is valid expression
                y = eval(self.user_input)
            except ValueError:   
                y = 1000000000
                x = self.computation_distance * self.graph_coord_size
                if eval(self.user_input) < 0:
                    y *= -1
            except:
                # exception called when the expression can not be evaluated (it isn't a valid expression)
                self.user_input = "SYNTAX ERROR!"
                self.update_display_area()
                break

            # precondition for this block: the expression is valid
            try:
                self.draw_line(x - self.computation_distance * self.graph_coord_size, y_previous, x, y)
            except:
                # this exception is thrown when x is raised to a non integer power
                #eval requires the pow function for this case
                self.user_input = "ERROR: Use pow(x) for non-int power values"
                self.update_display_area()
                break

            # store the to-coords to use as the next from-coords
            y_previous = y
            x += self.computation_distance * self.graph_coord_size

    def is_non_digit_ending_correct(self):
        # a valid function can end with non digit characters: x, e, pi, and )
        return self.user_input.endswith('x') or self.user_input.endswith('e') or (self.user_input.endswith('i') and self.user_input[-2:] != "si") or self.user_input.endswith(')')

    def is_ending_correct(self):
        # checks if the ending of the function is a digit or a valid non digit character
        return self.user_input[-1:].isdigit() or self.is_non_digit_ending_correct()

    def clear_input(self):
        self.user_input = ""
        self.update_display_area()

    def clear_error(self):
        if self.user_input == "SYNTAX ERROR!" or self.user_input == "ERROR: Use pow(x) for non-int power values":
            self.clear_input()

    def delete(self):

        self.clear_error()
        self.user_input = self.user_input[:-1]
        self.update_display_area()

    def append_number(self, number):

        self.clear_error()

        # multiply by number if the ending is a valid non digit character, e.g. sin(x)3 -> sin(x) * 3
        if self.is_non_digit_ending_correct():
            self.user_input += "*"

        # append the selected number to the input
        self.user_input += number
        self.update_display_area()

    def append_operator(self, operator):
        
        self.clear_error()

        # append the selected operator to the input
        self.user_input += operator
        self.update_display_area()

    # function for appending advanced characters like trig functions, variables, and constants (e, pi)
    def append_advanced(self, symbol):

        self.clear_error()

        # swap out 'π' to 'pi' for properly calling eval later
        if symbol == "π":
            symbol = "pi"

        # swap out 'x²'
        if symbol == "x²":
            symbol = "**2"

        if symbol == "pow(x)":
            symbol = "pow(x,"

        # eval wants log as log10
        if symbol == "log":
            symbol = "log10"

        # eval wants ln as just log
        if symbol == "ln":
            symbol = "log"

        # add an open parenthese to some of the symbols
        if symbol in ["sin", "cos", "tan", "log10", "log"]:
            symbol += "("


        if self.is_ending_correct():
            if symbol == "^":
                self.user_input += "**"
            elif symbol == "**2":
                self.user_input += symbol
            else:
                # case for things like 3log() -> 3 * log() or sin()log() -> sin() * log()
                self.user_input += ("*" + symbol)

        # just append input in the case of open parentheses or an operator being at the end        
        else:
            self.user_input += symbol
            
        self.update_display_area()

    def button_click_from_key(self, event):
        valid_keys = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", ".", "^", "(", ")", "BackSpace", "Enter", "Return", "x", "e"}

        key = event.char if event.char in valid_keys else event.keysym

        if key == "BackSpace":
            self.button_click("Del")
        elif key in valid_keys:
            self.button_click(key)
            