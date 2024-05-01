from tkinter import *
from PIL import ImageTk, Image

binDepth = 23

def binStatus(value):
    halfEmpty = binDepth/2 # 11.5
    nearFull = binDepth/4 # 5.75
    status = "Image/"

    if value <= nearFull:
        status += "FullBin.png"
    
    elif value <= halfEmpty and value > nearFull:
        status += "HalfBin.png"
    
    elif value > halfEmpty:
        status += "EmptyBin.png"

    return status

def calcPercentage(number):
    number = float(number)
    value = number/binDepth
    empty = value * 100
    fullness = 100 - empty
    fullness = round(fullness,2)
    return fullness

with open("Data/Measure1.txt","r") as file:
    reading1 = file.read()

with open("Data/Measure2.txt","r") as file:
    reading2 = file.read()

with open("Data/Measure3.txt","r") as file:
    reading3 = file.read()

# Calculation for the GUI
bin1Status = binStatus(float(reading1)) 
bin2Status = binStatus(float(reading2)) 
bin3Status = binStatus(float(reading3))
percent1 = calcPercentage(reading1)
percent2 = calcPercentage(reading2)
percent3 = calcPercentage(reading3)

window = Tk() 
window.title("Smart Bins Dashboard") # Set the title of the window

# Set the window info
title = Label(window, text="Smart Bins")
window.iconbitmap("Image/SmartBinIcon.ico")

# Set the widgets
bin1Title = Label(window, text="Organic", width=25)
bin1Label = Label(window, text="Bin 1", width=25)
info1 = Label(window,text=f"Percentage full: {percent1}%")
bin2Title = Label(window, text="Mixed", width=25)
bin2Label = Label(window, text="Bin2", width=25)
info2 = Label(window,text=f"Percentage full: {percent2}%")
bin3Title = Label(window, text="Recycle", width=25)
bin3Label = Label(window, text="Bin 3", width=25)
info3 = Label(window,text=f"Percentage full: {percent3}%")
exitBtn = Button(window,text="Exit Program", command=window.quit)

# Image selection and display 
img1 = ImageTk.PhotoImage(Image.open(bin1Status))
img2 = ImageTk.PhotoImage(Image.open(bin2Status))
img3 = ImageTk.PhotoImage(Image.open(bin3Status))

status1 = Label(image=img1,width=160, height=350)
status2 = Label(image=img2,width=160, height=350)
status3 = Label(image=img3,width=160, height=350)

# Place them in the window using the grid method
title.grid(row=0,column=0,columnspan=3)
bin1Title.grid(row=1,column=0)
bin2Title.grid(row=1,column=1)
bin3Title.grid(row=1,column=2)
bin1Label.grid(row=2,column=0)
bin2Label.grid(row=2,column=1)
bin3Label.grid(row=2,column=2)
status1.grid(row=3,column=0)
status2.grid(row=3,column=1)
status3.grid(row=3,column=2)
info1.grid(row=4,column=0)
info2.grid(row=4,column=1)
info3.grid(row=4,column=2)
exitBtn.grid(row=5,column=1)

window.mainloop()