print("a is", a := int(input("Enter value of a:")),
      "b is", b := int(input("Enter value of b:")),
      "c is", c := int(input("Enter value of c:")))

if a == b == c:
    print("a, b and c are of the same value")
elif a > b and a > c:
    print("a is the greatest number")
elif b > a and b > c:
    print("b is the greatest number")
elif c > a and c > b:
    print("c is the greatest number")
