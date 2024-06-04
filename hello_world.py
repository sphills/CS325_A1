print("Hello world!")

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def honk(self):
        print("\"HONK HOOOOONK!\" goes the", self.color.lower(), self.brand + ".")

sedan = Car("Toyota", "Black")

sedan.honk()