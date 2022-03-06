import string
 
def IsPangram(UserWord):
    Letters = set(string.ascii_lowercase)
    return set(UserWord.lower()) >= Letters
 
 
UserInput = input("Enter a sentence: ")
if IsPangram(UserInput) == True:
    print("This is a pangram")
else:
    print("This isn't a pangram")
