from tkinter import *
MainWindow = Tk()
MainWindow.title('MyWidget')
Widget = Canvas(MainWindow, bg = "red", width = 400, height = 400)
Widget.pack()
n = Label(MainWindow, text="Hello World", font=("Times New Roman", 18))
n.pack()
MainWindow.mainloop()
