MyList = [0,1,2,3,4,5,6,7,8,9,10]
Poppers = [0,2,4,5]
 
y = 0
for x in Poppers:
    MyList.pop(x-y)
    y+=1
 
print(MyList)