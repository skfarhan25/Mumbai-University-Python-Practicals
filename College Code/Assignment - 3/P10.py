from tkinter import *
MainWindow = Tk()
MainWindow.title("Edit Menu")
MainWindow.geometry("400x400")

text = Text(MainWindow, undo=True)
text.insert(INSERT, "Type Something")
text.pack()

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def delete():
    text.delete(SEL_FIRST, SEL_LAST)

def select_all():
    text.tag_add(SEL, "1.0", END)

def about():
    about_window = Toplevel(MainWindow)
    about_window.title("About")
    about_window.configure(background="white")
    about_label = Label(about_window, text=
"""This is a text editor made by me using python 3.10.1 64-bit
It uses the tkinter library.
It was made in Visual Studio Code.
This is a GUI application.
It has a menu bar with edit, help and exit options.
Menu bar has an edit menu with undo, cut, copy, paste, delete, select all options.
Help menu has an about section.
Undo option undoes the last action.
Cut option cuts the selected text.
Copy option copies the selected text.
Paste option pastes the copied text.
Delete option deletes the selected text.
Select All option selects all the text.
About option displays the about window.""", bg="white", justify=LEFT)
    about_label.pack()

def help():
    print("This is a text widget")

def exit():
    MainWindow.destroy()


menu = Menu(MainWindow)

submenu = Menu(menu)
submenu.add_command(label="Undo", command=text.edit_undo)
submenu.add_command(label="Cut", command=cut)
submenu.add_command(label="Copy", command=copy)
submenu.add_command(label="Paste", command=paste)
submenu.add_command(label="Delete", command=delete)
submenu.add_command(label="Select All", command=select_all)

menu.add_cascade(label="Edit", menu=submenu)

helpmenu = Menu(menu)
helpmenu.add_command(label="About", command=about)
menu.add_cascade(label="Help", menu=helpmenu)

MainWindow.config(menu=menu)

MainWindow.mainloop()