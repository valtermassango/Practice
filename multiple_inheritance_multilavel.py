#multiple inheritance is when a class can be derived from more than one base class. The derived class inherits the features of all the base classes.
#multilavel inheritance is when a class is derived from a base class, which is also derived from another base class. The derived class inherits the features of both the base classes.
class Animal:
   def __init__(self, name):
         self.name = name

   def eat(self):
       print(f"{self.name} is eating.")

   def sleep(self):
        print(f"{self.name} is sleeping.")

   
class Prey (Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class Predator (Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

class Rabbit (Prey):
    pass

class Hawk (Predator):
    pass

class Fish (Prey, Predator) :
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()
fish.sleep()  
hawk.hunt()
fish.hunt()