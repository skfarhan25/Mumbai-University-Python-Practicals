def fact(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * fact(n - 1)

UserInput = int(input("Enter a Number: "))
print("Factorial of", UserInput, "is", fact(UserInput))