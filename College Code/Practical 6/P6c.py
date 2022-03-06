UserInput = int(input("How many last lines would you like to read?\n"))

with open("Python\\College Code\\Practical 6\\P6c.txt", "r") as MyFile3:
    LinesList = MyFile3.readlines(0)
    for i in range(1, UserInput + 1):
        Line = LinesList[-i]
        print(Line, end = "")
