from tkinter import *
from tkinter import messagebox

MainWindow = Tk()
MainWindow.title('MyButton')

def HelloCallBack():
    messagebox.showinfo('Hello Python', 'Hello World')

MyButton = Button(MainWindow, text='Hello', command=HelloCallBack, width=35, height=2)
MyButton.pack()
MainWindow.mainloop()