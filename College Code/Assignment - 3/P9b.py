from tkinter import *
MainWindow = Tk()
MainWindow.title('College Form')

# Functions
def RadioButtonCheck():
    global StreamName
    if Stream.get() == 1:
        StreamName = "Science"
    elif Stream.get() == 2:
        StreamName = "Commerce"
    elif Stream.get() == 3:
        StreamName = "Arts"

def CheckBoxCheck():
    global LanguageName
    LanguageName = ""
    if CPP.get() == 1:
        LanguageName += " C++"
    if Python.get() == 1:
        LanguageName += " Python"
    if CSharp.get() == 1:
        LanguageName += " C#"

def On_SubmitButton_Click():
    Overall_Result.set(f"""
    Student Name: {StudentName_Entry.get()},
    Stream: {StreamName},
    Languages: {LanguageName},
    SSC Score: {SSC_Percentage.get()}""")

# Variables
Greeting = StringVar()
Greeting.set("Hello, This is a College Form\n Please fill in the details below")

CPP, Python, CSharp = IntVar(), IntVar(), IntVar()

Student_Name = StringVar()
Stream = IntVar()
SSC_Percentage = DoubleVar()
Overall_Result = StringVar()

My_Greeting_Label = Label(MainWindow, textvariable=Greeting, relief=RAISED, width=35, height=2)
My_Greeting_Label.pack()

StudentName_Label = Label(MainWindow, text="Student Name:", textvariable=Student_Name, width=35, height=2)
StudentName_Label.pack()
StudentName_Entry = Entry(MainWindow, bd=5)
StudentName_Entry.insert(0, "Enter your name here")
StudentName_Entry.pack()

My_Science_RadioButton = Radiobutton(MainWindow, text='Science', variable=Stream, value=1, height=2, width=20, command=RadioButtonCheck)
My_Science_RadioButton.pack()
My_Commerce_RadioButton = Radiobutton(MainWindow, text='Commerce', variable=Stream, value=2, height=2, width=20, command=RadioButtonCheck)
My_Commerce_RadioButton.pack()
My_Arts_RadioButton = Radiobutton(MainWindow, text='Arts', variable=Stream, value=3, height=2, width=20, command=RadioButtonCheck)
My_Arts_RadioButton.pack()

My_CPP_CheckButton = Checkbutton(MainWindow, text='C++', variable=CPP, onvalue=1, offvalue=0, height=2, width=20, command=CheckBoxCheck)
My_CPP_CheckButton.pack()
My_Python_CheckButton = Checkbutton(MainWindow, text='Python', variable=Python, onvalue=1, offvalue=0, height=2, width=20, command=CheckBoxCheck)
My_Python_CheckButton.pack()
My_CS_CheckButton = Checkbutton(MainWindow, text='C#', variable=CSharp, onvalue=1, offvalue=0, height=2, width=20, command=CheckBoxCheck)
My_CS_CheckButton.pack()

My_SSC_Score_Scale = Scale(MainWindow, from_=0, to=100, orient=HORIZONTAL, variable=SSC_Percentage, length=200)
My_SSC_Score_Scale.pack()

My_Submit_Button = Button(MainWindow, text='Submit', command=On_SubmitButton_Click, width=10, height=1)
My_Submit_Button.pack()

My_Result_Label = Label(MainWindow, textvariable=Overall_Result)
My_Result_Label.pack()

MainWindow.mainloop()
