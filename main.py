# HOWS TO IMPORT TKINTER IN PYTHON
import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# HOW TO CREATE A LABEL
my_label = tkinter.Label(text="I'm just learning GUI", font=("Arial", 24, "bold"))
my_label.pack()


window.mainloop()
