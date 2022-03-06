a = (1,2,3,4)
b = (5,6,7,8)
c = a + b
temp = list(c)
temp.sort()
d = tuple(temp)
print(f"Third element of tuple d is {d[3]}")
print(f"Last three elements of tuple d: {d[:-4:-1]}")
print(len(d))
