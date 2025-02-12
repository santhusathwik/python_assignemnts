class Car:
    total_cars=0

    def __init__(self,model,year,price):
        self.model=model
        self.year=year
        self.price=price

        Car.total_cars+=1
    
    #instance method
    def car_info(self):
        print(f"Car details {self.model} {self.year} {self.price}")
    
    #class method
    @classmethod
    def get_total_cars(cls):
        print(f"Total cars are:{cls.total_cars}")
    
    @staticmethod
    def calculate_depreciation(price,year):
        rate=0.15
        value=price*((1-rate)**year)
        return value
    
#creating instances for the car class
car1=Car("Toyota",2020,2500000)
car2=Car("Mahindr",2023,500000)

#instance variables
car1.car_info()
car2.car_info()

#class variables
Car.get_total_cars()

value=Car.calculate_depreciation(25000,3)
print(f"Depreciated Value {value}")