from tkinter import *
MainWindow = Tk()
MainWindow.title('MyEntry')
MyLabel = Label(MainWindow, text="Enter your Username:", width=35, height=2)
MyLabel.pack()
MyEntry = Entry(MainWindow, bd=5)
MyEntry.pack()
MainWindow.mainloop()