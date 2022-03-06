class Numbers():

    MULTIPLIER = 2

    def __init__(self, MULTIPLIER):
        self.MULTIPLIER = MULTIPLIER

    def add(self,x,y):
        self.x = x
        self.y = y
        return x + y

    def multiply(self, a):
        return a * self.MULTIPLIER

    def subtract(b, c):
        return b - c

    def value(self):
        return (self.x, self.y)

    def setter(self, x , y):
        self.x = x
        self.y = y
        print(f"x set to {x}, y set to {y}")

    def getter(self):
        return self.x, self.y


MyObj = Numbers(2)
x,y = int(input("Enter value of x: ")), int(input("Enter value of y: "))

print(f"Addition of x and y Numbers: {MyObj.add(x,y)}")
print(f"Subtraction of x and y Number: {Numbers.subtract(x,y)}")
print(f"Tuple: {MyObj.value()}")
MyObj.setter(10,5)
print(f"Getter: {MyObj.getter()}")