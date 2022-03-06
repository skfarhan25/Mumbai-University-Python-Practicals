while True:
    UserInput = int(input("Enter a 4 digit: "))

    if len(str(UserInput)) < 4 or len(str(UserInput)) > 4:
        print("Error: Number has to be 4 digit")
        continue
    else:
        break

sum = 0
for x in str(UserInput):
    sum += int(x)

print("Sum of digits:", sum)

