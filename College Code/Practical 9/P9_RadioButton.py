# RadioButton in Tkinter
from tkinter import *
MainWindow = Tk()
MainWindow.title('MyRadioButton')
MainWindow.geometry('300x150')

var = IntVar()

RadioButton1 = Radiobutton(MainWindow, text='Science', variable=var, value=1, height=2, width=20)
RadioButton2 = Radiobutton(MainWindow, text='Commerce', variable=var, value=2, height=2, width=20)
RadioButton3 = Radiobutton(MainWindow, text='Arts', variable=var, value=3, height=2, width=20)

RadioButton1.pack()
RadioButton2.pack()
RadioButton3.pack()

MainWindow.mainloop()