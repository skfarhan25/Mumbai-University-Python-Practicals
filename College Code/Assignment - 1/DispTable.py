num = int(input("Enter a Number: "))
i = 0
for x in range(num, (num*10)+1, num):
    i += 1
    print(num, "x", i, "=", x)


# Optional method
# x = 1
# while x < 11:
#     if num == 0:
#         print("0 multiplied by any number is 0")
#         break
#     print(num, "x", x, "=", num * x)
#     x += 1
