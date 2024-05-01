from tkinter import *

window = Tk() 
window.title("Smart Bins Dashboard") # Set the title of the window

# Set the widgets
title = Label(window, text="Smart Bins")
bin1Title = Label(window, text="Organic")
bin2Title = Label(window, text="Mixed")
bin3Title = Label(window, text="Recycle")

# Place them in the window using the grid method
title.grid(row=0,column=0,columnspan=3)
bin1Title.grid(row=1,column=0)
bin2Title.grid(row=1,column=1)
bin3Title.grid(row=1,column=2)

window.mainloop()