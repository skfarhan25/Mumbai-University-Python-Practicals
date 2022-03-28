from tkinter import *
MainWindow = Tk()
MainWindow.title('MyMessageBox')
var = StringVar()
MyLabel = Label(MainWindow, textvariable=var, relief=RAISED, width=35, height=1)
var.set("Hello World")
MyLabel.pack()
MainWindow.mainloop()

