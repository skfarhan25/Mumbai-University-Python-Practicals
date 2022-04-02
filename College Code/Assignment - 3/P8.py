try:
    Num1 = int(input("Enter a number: "))
    Num2 = int(input("Enter a second number: "))
    print(f"The Result is {Num1/Num2}")
except ZeroDivisionError:
    print("Error: Cannot Divide by 0")
except (TypeError, NameError, ValueError):
    print("Error ocurred")
finally:
    print("Thank You!")

    