def Fibonacci(num):
    if num <= 1:
        return num
    else:
        return Fibonacci(num - 1) + Fibonacci(num - 2)


UserInput = int(input("Enter a Number: "))

if UserInput <= 0: print("Enter a number greater than 0")
else:
    print("Fibonacci sequence:")
    for i in range(UserInput):
        print(Fibonacci(i))