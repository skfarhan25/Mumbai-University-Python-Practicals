def isPalindrome(Num):
    if Num == str(Num[::-1]):
        return True
    else:
        return False


def isArmstrong(Num):
    i = 0
    for x in Num:
        i += int(x) ** len(Num)
    if str(i) == Num:
        return True
    else:
        return False


UserInput = int(input("Enter a Number: "))

if isPalindrome(str(UserInput)) == True:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

if isArmstrong(str(UserInput)) == True:
    print("The number is a armstrong")
else:
    print("The number is not a armstrong")