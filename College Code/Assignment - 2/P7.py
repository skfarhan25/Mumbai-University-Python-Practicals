a = [1, 3, 5]
b = [0, 2, 4]
c = a + b
d = c.copy()
d.sort()
d.sort(reverse = True)
c[4] = 42
d.append(10)
c.extend([7,8,9])
print(f"First three elements of list c: {c[0:3]}")
print(f"Last element of list d: {d[::-1]}")
print(f"Length of d: {len(d)}")

