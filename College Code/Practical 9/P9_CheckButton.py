from tkinter import *
MainWindow = Tk()
MainWindow.title('MyCheckButton')
MainWindow.geometry('300x150')

Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()

Checkbutton1 = Checkbutton(MainWindow, text='C++', variable=Var1, onvalue=1, offvalue=0, height=2, width=20)
Checkbutton2 = Checkbutton(MainWindow, text='Python', variable=Var2, onvalue=1, offvalue=0, height=2, width=20)
Checkbutton3 = Checkbutton(MainWindow, text='C#', variable=Var3, onvalue=1, offvalue=0, height=2, width=20)

Checkbutton1.pack()
Checkbutton2.pack()
Checkbutton3.pack()

MainWindow.mainloop()