from tkinter import *

window = Tk() 
window.title("Smart Bins Dashboard") # Set the title of the window

# Set the widgets
title = Label(window, text="Smart Bins")

# Place them in the window using the grid method
title.grid(row=0,column=0,columnspan=3)

window.mainloop()