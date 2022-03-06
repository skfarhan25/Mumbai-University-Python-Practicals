def FindLength(word):
    return len(word)

MyList = list(range(1,11))
UserInput = input("Enter a word: ")
print(f"Length of the string is {FindLength(UserInput)}")
print(f"Length of the string is {FindLength(MyList)}")