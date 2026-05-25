#Abstract Class is a class that cannot be instantiated and is typically used as a base class for other classes. It can contain abstract methods, which are methods that are declared but not implemented in the abstract class. Subclasses of the abstract class must provide an implementation for the abstract methods.
#The benefit of using an abstract class is:
#1. It provides a common interface for all subclasses, ensuring that they implement the same methods.
#2. It allows for code reuse, as common functionality can be implemented in the abstract class and shared among all subclasses.
#3. Prevents the instantiation of the abstract class, ensuring that only concrete subclasses can be instantiated.
#4. Reqires childre to use inherited abstract methods, which can help to enforce a certain design or structure in the code.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go (self):
        pass

    @abstractmethod
    def stop (self):
        pass

vehicle = Vehicle() # This will raise an error because we cannot instantiate an abstract class
