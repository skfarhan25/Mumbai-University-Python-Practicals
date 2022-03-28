# Scale in Tkinter
from tkinter import *
MainWindow = Tk()
MainWindow.title('MyScale')
MainWindow.geometry('300x150')

var = DoubleVar()

MyScale = Scale(MainWindow, variable=var)
MyScale.pack()
# Show the value of the scale when the button is clicked using entry
MyEntry = Entry(MainWindow, textvariable=var)
MyEntry.pack()
MyButton = Button(MainWindow, text='Submit', command=lambda: print(var.get()))
MyButton.pack()

MainWindow.mainloop()