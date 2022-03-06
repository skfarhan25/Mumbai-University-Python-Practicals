def Factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num > 1:
        return num * Factorial(num - 1)


UserInput = int(input("Enter a Number: "))
print(f"Factorial of {UserInput} is {Factorial(UserInput)}")