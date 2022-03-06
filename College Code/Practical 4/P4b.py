MyList = list(range(11))
print(MyList)
Poppers = [0,2,4,5]


y = 0
for x in Poppers:
    MyList.pop(x-y)
    y += 1


print(MyList)