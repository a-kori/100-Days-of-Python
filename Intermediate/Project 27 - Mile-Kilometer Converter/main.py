import tkinter

window = tkinter.Tk()
window.title("My Program")
window.minsize(width=600, height=600)

my_label = tkinter.Label(text="I am a label.", font=("Arial", 24, "bold"))
my_label.pack()




window.mainloop()
