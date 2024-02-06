# 1. შექმენით პითონის კლასი Car, ატრიბუტებით ბრენდით, მოდელით და წლით. ასევე, შექმენით კლასის მეთოდი car_info(),
#  რომელიც დაბეჭდავს ატრიბუტების ინფორმაციას.

# 2. Car კლასში დაამატეთ მეთოდი age_of_car, რომელიც დაითვლის მანქანის ასაკს.

# 3. შექმენით კლასი ElectricCar, რომელიც მემკვიდრეობით მიიღებს Car class-ს. დაამატეთ ახალი ატრიბუტი battery_life და მეთოდი
#  battery_info(), რომელიც დაბეჭდავს შემდეგ სტრიქონს "ამ მანქანის ბატარეის ხანგრძლივობა არის [battery_life] საათი".

# 4. დაამატეთ Car კლასს ატრიბუტი number_of_cars, რომელიც დაითვლის მანქანების სრულ რაოდენობას. გაზარდეთ ეს ცვლადი ყოველ ჯერზე, \
# მანქანის შექმნისას. 

# 5. Car კლასს დაამატეთ მეთოდი total_cars(), რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.


class Car:
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.number_of_cars += 1

    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

    def age_of_car(self, current_year):
        return current_year - self.year

    @classmethod
    def total_cars(cls):
        print(f"Total number of cars: {cls.number_of_cars}")


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"This car has {self.battery_life} percentage battery life.")


car1 = Car("Toyota", "Camry", 2018)
car2 = Car("Tesla", "Model S", 2020)
car3 = ElectricCar("Nissan", "Leaf", 2019, 85)

Car.total_cars()  

car1.car_info()  
print(f"Age of car: {car1.age_of_car(2023)} years") 

car3.battery_info() 

