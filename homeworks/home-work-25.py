class BookDetails:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class DiscountCalculator:
    def get_discount_price(self, book, discount):
        pass



#2
    
class Payment:
    """Payment class"""
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    """Credit card payment process"""
    def process_payment(self, amount):
        pass

class PayPalPayment(Payment):
    """PayPal payment process"""
    def process_payment(self, amount):
        pass


#3
class Vehicle:
    def fuel_capacity(self):
        return 100  

class ElectricCar(Vehicle):
    def fuel_capacity(self):
        return 100
    

#4
    
class AudioPlayer:
    def play_audio(self):
        pass

class VideoPlayer:
    def play_video(self):
        pass

#5
    
from abc import ABC, abstractmethod

class Display(ABC):
    @abstractmethod
    def show(self, data):
        pass

class ConsoleDisplay(Display):
    def show(self, data):
        print(data)

class WeatherStation:
    def __init__(self, display):
        self.display = display

    def report(self):
        self.display.show("Weather Data")