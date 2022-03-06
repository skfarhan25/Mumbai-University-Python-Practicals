def reverse_number(num):
    return str(num[::-1])

UserInput = int(input("Enter a Number: "))
print("Reverse of the number is", reverse_number(str(UserInput)))