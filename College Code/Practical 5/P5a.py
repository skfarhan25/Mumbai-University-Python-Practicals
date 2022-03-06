MyDict = {1: 30, 2: 50, 3: 20, 4: 100, 5: 70,
          6: 90, 7: 80, 8: 60, 9: 10, 10: 40}

# Initialise the List
# Add Values of Dictionary to List using list comprehension
MyList = [MyDict[x] for x in MyDict]

AscendingOrDescending = input("Would you like the list to be ascending? (y/n)\n")
# Sort the list
if AscendingOrDescending == "y":
    MyList.sort()
else:
    MyList.sort(reverse = True)

# Add elements of List to Dictionary
for x in MyDict:
    MyDict[x] = MyList[x-1]

print(MyDict)
