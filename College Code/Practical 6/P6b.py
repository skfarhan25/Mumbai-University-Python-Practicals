with open("Python\\College Code\\Practical 6\\P6b.txt", "a+") as MyFile2:
    MyFile2.write("\nThis sentence has ben appended using Python")
    MyFile2.seek(0)
    print(MyFile2.read())