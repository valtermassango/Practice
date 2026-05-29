class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
    
    def discribe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, filled,radius):
        super().__init__(color, filled)  # Call the constructor of the superclass
        self.radius = radius

    def discribe(self):
       super().discribe() # Call the describe method of the superclass
       print(f"It is a circle with area of {3.14 * self.radius ** 2:.2f} cm^2 and circumference of {2 * 3.14 * self.radius:.2f} cm")
        

   
class Square(Shape):
    def __init__(self, color, filled,width):
        super().__init__(color, filled)  # Call the constructor of the superclass
        self.width = width

    def discribe(self):        
        super().discribe() # Call the describe method of the superclass
        print(f"It is a square with area of {self.width ** 2} cm^2 and perimeter of {4 * self.width} cm")

class Triangle(Shape):
    def __init__(self, color, filled,width,height):
        super().__init__(color, filled)  # Call the constructor of the superclass
        self.width = width
        self.height = height
    def discribe(self):
        super().discribe() # Call the describe method of the superclass
        print(f"It is a triangle with area of {0.5 * self.width * self.height} cm^2 and perimeter of {self.width + self.height + (self.width ** 2 + self.height ** 2) ** 0.5} cm")


circle = Circle("red", True, 5)
square = Square("blue", False, 4)
triangle = Triangle("green", True, 3, 4)


#circle.discribe()
#square.discribe()
triangle.discribe()