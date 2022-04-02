class Shape:
    
    def __init__(self) -> None:
        print("Operating")

class Square(Shape):
    
    def area(self, side):
        return side ** 2

MyObj = Square()
print(f"Area of a square {MyObj.area(5)}")