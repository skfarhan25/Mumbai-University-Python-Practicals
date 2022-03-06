def isPalindrome(num):
    if num == str(num[::-1]):
        return True
    else:
        return False

def isArmstrong(num):
    a = 0
    for x in num:
        a += int(x) ** len(num)
    if str(a) == num:
        return True
    else:
        return False

UserInput = int(input("Enter a Number: "))

if isPalindrome(str(UserInput)) == True:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

if isArmstrong(str(UserInput)) == True:
    print("The number is a Armstrong.")
else:
    print("The number is not a Armstrong.")
