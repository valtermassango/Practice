# Inheritance is a fundamental concept in object-oriented programming that allows a new class (called a child or subclass) to inherit attributes and methods from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.
# The child class can also have its own unique attributes and methods, in addition to the inherited ones. This allows for specialization and extension of the parent class's functionality.
#Inheritance allows a class to inherit attibuites and methods from another class, helps to code reusabilitiy and extensibility.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog (Animal):
    def speak(self):
        print(f"{self.name} says Woof!")


class Cat (Animal):
    def speak(self):
        print(f"{self.name} says Meow!")  

class Mouse (Animal):
    def speak(self):
        print(f"{self.name} says Squeak!")

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Siamese")
mouse = Mouse("Squeaky", "House Mouse")

print(dog.name) # Output: Buddy
print(cat.species) # Output: Siamese
dog.eat() # Output: Buddy is eating.
cat.sleep() # Output: Whiskers is sleeping.


dog.speak() # Output: Buddy says Woof!
cat.speak() # Output: Whiskers says Meow!
mouse.speak() # Output: Squeaky says Squeak!
