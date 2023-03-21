from tkinter import *

# Window configuration
window = Tk()
window.title("Mile-Kilometer Converter")
window.config(padx=25, pady=25)

# Miles and kilometers entries
miles_entry = Entry(width=20)
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)

km_entry = Entry(width=20)
km_entry.insert(END, string="0")
km_entry.grid(column=1, row=1)
km_entry.config(state=DISABLED)

# Labels
Label(text="Miles").grid(column=2, row=0)
Label(text="is equal to").grid(column=0, row=1)
Label(text="Km").grid(column=2, row=1)

# Radio buttons
def radio_used():
    '''Changes the unit to be converted depending on the radio button selected.'''
    if radio_state.get() == 0:
        km_entry.config(state=DISABLED)
        miles_entry.config(state=NORMAL)
    else:
        km_entry.config(state=NORMAL)
        miles_entry.config(state=DISABLED)

radio_state = IntVar()
miles_km = Radiobutton(text="Miles to Km", value=0, variable=radio_state, command=radio_used)
km_miles = Radiobutton(text="Km to Miles", value=1, variable=radio_state, command=radio_used)
miles_km.grid(column=0, row=2)
km_miles.grid(column=1, row=2)

# Calculate button
def replace_text(entry: Entry, new_text: str):
        '''Replaces the current text in entry with new_text.'''
        if entry["state"] == DISABLED:
            entry.config(state=NORMAL)
            entry.delete(0, END)
            entry.insert(END, new_text)
            entry.config(state=DISABLED)
        else:
            entry.delete(0, END)
            entry.insert(END, new_text)

def convert():
    '''Converts one unit to another (miles-km / km-miles) depending on the active radio button.'''
    try:
        if radio_state.get() == 0:
            km = float(miles_entry.get()) * 1.6
            replace_text(km_entry, int(km) if int(km) == km else km)
        else:
            miles = float(km_entry.get()) / 1.6
            replace_text(miles_entry, int(miles) if int(miles) == miles else miles)
    except:
        replace_text(km_entry, "ERROR")
        replace_text(miles_entry, "ERROR")

calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=2, row=2)

window.mainloop()
