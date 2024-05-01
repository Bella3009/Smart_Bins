from tkinter import *

window = Tk() 
window.title("Smart Bins Dashboard") # Set the title of the window

# Set the window info
title = Label(window, text="Smart Bins")
window.iconbitmap("SmartBinIcon.ico")

# Set the widgets
bin1Title = Label(window, text="Organic", width=25)
bin1Label = Label(window, text="Bin 1", width=25)
bin2Title = Label(window, text="Mixed", width=25)
bin2Label = Label(window, text="Bin2", width=25)
bin3Title = Label(window, text="Recycle", width=25)
bin3Label = Label(window, text="Bin 3", width=25)

# Place them in the window using the grid method
title.grid(row=0,column=0,columnspan=3)
bin1Title.grid(row=1,column=0)
bin2Title.grid(row=1,column=1)
bin3Title.grid(row=1,column=2)
bin1Label.grid(row=2,column=0)
bin2Label.grid(row=2,column=1)
bin3Label.grid(row=2,column=2)

window.mainloop()