# Class Variables = Shared by all instances of the class
# Instance Variables = Unique to each instance of the class 
# Methods = Functions that are defined inside a class and can be called on an instance of the class
# Self = Represents the instance of the class and is used to access the attributes and methods of the class
# Init method = A special method that is called when an instance of the class is created and
# variables defined in the init method are called instance variables and are unique to each instance of the class
# variable defined outside the constructor are called class variables and are shared by all instances of the class.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
student1 = Student("John", 20, "A")
student2 = Student("Jane", 21, "B")

print(student1.name) # Output: John
print(student2.name) # Output: Jane
