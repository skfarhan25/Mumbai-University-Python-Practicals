def Reversi(UserValue):
    return UserValue[::-1]


UserInput = input("Enter Something: ")
print(f"Reverse of the input is {Reversi(UserInput)}")
