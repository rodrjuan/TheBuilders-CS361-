from tkinter import *
from tkinter import ttk

def copy_to_clipboard(event, text):
 
    #get the index of the line based on coordinates of mouse
    index = text.index("@%s,%s" % (event.x, event.y))
    line, char = index.split(".")

    nextline = int(line) + 1

    text.clipboard_clear()

    #starts from first char of the line, stops at first char of next line
    string = text.get(f'{line}.0', f'{nextline}.0')
    text.clipboard_append(string.strip())  

def show_memory(calculations):

    #create second window
    memory = Toplevel()
    memory.title("Calculation History")
    memory.geometry("400x600")

    text = Text(memory, cursor="arrow", font=("Helvetica", 12))

    #create a line of text for every calculation
    for i, calculation in enumerate(calculations):
        text.insert(f'{i + 1}.0', f'{calculation}\n')

    #create callback function that copys line of text to clipboard on click
    text.bind("<Button-1>", lambda e:copy_to_clipboard(e, text))

    text.pack(expand=TRUE, fill=BOTH)

    #display a scrollbar on the right side
    scrollbar = Scrollbar(memory, orient = VERTICAL, command = text.yview)
    text.configure(yscrollcommand = scrollbar.set)
    scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor= "ne")