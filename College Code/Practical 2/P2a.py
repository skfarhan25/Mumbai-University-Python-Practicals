def FindVowel(word):

    VowelList = ["a","e","i","o","u"]

    if any(vowel for vowel in word if vowel in VowelList):
        return True
    else:
        return False


UserInput = input("Enter a Number: ")
UserInput = UserInput.lower()
if FindVowel(UserInput) == True:
    print("There is a vowel")
else:
    print("There isn't vowel")