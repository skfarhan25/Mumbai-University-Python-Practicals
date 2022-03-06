class NumberCheck():
    
    def __init__(self):
        print("Base Class:")

    def EvenOrOdd(self, num):
        print("The Number is Even" if num % 2 == 0 else "The Number is Odd")


class Operation(NumberCheck):

    def __init__(self):
        print("Derived Class:")

    def Double(self, num):
        print(f"Double of {num} is {num ** 2}")
    
    
BaseObj = NumberCheck()
BaseObj.EvenOrOdd(2)
BaseObj.EvenOrOdd(3)

DerivedObj = Operation()
DerivedObj.EvenOrOdd(4)
DerivedObj.EvenOrOdd(5)
DerivedObj.Double(5)