def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


UserInput = int(input("Enter a Number: "))

if UserInput <= 0:
    print("Enter a number greater than 0")
else:
    print("Fibonacci sequence:")
    for i in range(UserInput):
        print(fibonacci(i))