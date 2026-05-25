# Super Class is a class that is inherited by another class, known as the subclass. The subclass can override or    extend the functionality of the super class. The benefit of using a super class is: 
# 1. Code Reusability: The super class can be reused by multiple subclasses, reducing code duplication.
# 2. Maintainability: Changes to the super class are automatically reflected in all subclasses.
# 3. Polymorphism: Subclasses can override methods of the super class, allowing for different behaviors based on the object type.

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

class Circle(Shape):
    def area(self, color, filled,radius):
        super().__init__(color, filled)
        self.radius = radius


class Square(Shape):
    def area(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

class Triangle(Shape):
    def area(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

circle = Circle(color="red", filled=True, radius=5)
