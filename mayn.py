class Car:
    def __init__(self, make, model, year, color, for_sale):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.For_sale = for_sale
        
car1= Car("Toyota", "Camry", 2020, "Red", True)       
car2= Car("Honda", "Civic", 2019, "Blue", False)
car3= Car("Ford", "Mustang", 2021, "Black", True)

print(car1.make)
print(car2.model)
print(car3.year)
print(car1.color)
print(car2.For_sale)
print(car3.For_sale)    