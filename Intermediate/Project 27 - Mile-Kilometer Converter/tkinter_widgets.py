from tkinter import *

# New window
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)


# Label
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()


# Button (calls action() when pressed)
def action():
    print("Do something")

button = Button(text="Click Me", command=action)
button.pack()


# Single-line text entry
entry = Entry(width=30)
    # Adds starting text.
entry.insert(END, string="Some text to begin with.")
    # Gets text in input field.
print(entry.get())
entry.pack()


# Multi-line text entry
text = Text(height=5, width=30)
    # Puts cursor in textbox.
text.focus()
    # Adds starting text.
text.insert(END, "Example of multi-line text entry.")
    # Gets current input in textbox at line 1, character 0.
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    '''Prints the current value in spinbox.'''
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    '''Requires (!) and prints the current scale value.'''
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Check button
def checkbutton_used():
    '''Prints 1 if button is checked, otherwise 0.'''
    print(checked_state.get())

# Variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()


# Radio button
def radio_used():
    '''Prints 1 if button is checked, otherwise 0.'''
    print(radio_state.get())

# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# List box
def listbox_used(event):
    '''Gets current selection from listbox.'''
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
