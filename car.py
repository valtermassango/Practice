class Car:
    def __init__(self, make, model, year, color, for_sale):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.For_sale = for_sale

    def drive(self):
        print(f"You drive the {self.year} {self.make} {self.model}")
        # {self.attribute} is called placeholder and is used to access the attributes of the class and print them in the string

    def stop(self):
        print(f"You stop the {self.year} {self.make} {self.model}")

