with open("C://Users//admin//VSCode//Python//College Code//Assignment - 3//P1.txt", "w+") as MyFile1:
    MyFile1.write("Hello World!\nThis is a file written in Python!")
    MyFile1.seek(0)
    print(MyFile1.read())

