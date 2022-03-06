with open("Python\\College Code\\Practical 6\\P6a.txt", "w+") as MyFile1:
    MyFile1.write("Hello World!\nThis is a file written in Python!")
    MyFile1.seek(0)
    print(MyFile1.read())
