#Assignment

class Smartphone:
    def __init__(self, brand, model, storage, battery_level):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_level = battery_level
    
    def display_info(self):
        return f"{self.brand} {self.model}, Storage: {self.storage}GB, Battery: {self.battery_level}%"
    
    def check_battery(self):
        if self.battery_level > 20:
            return f"Battery is good ({self.battery_level}%)"
        else:
            return f"Battery is low, please charge! ({self.battery_level}%)"
    
    def make_call(self, number):
        return f"Calling {number}... 📞"

class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage, battery_level, camera_resolution):
        super().__init__(brand, model, storage, battery_level)
        self.camera_resolution = camera_resolution
    
    def take_photo(self):
        return f"Taking a photo with {self.camera_resolution} MP camera 📸"
    
    def make_call(self, number):
        return f"Calling {number}... But first, let me take a selfie! 📸"

phone1 = Smartphone("Apple", "iPhone 13", 128, 85)
print(phone1.display_info())
print(phone1.check_battery())
print(phone1.make_call("123-456-7890"))

phone2 = SmartphoneWithCamera("Samsung", "Galaxy S21", 256, 75, 108)
print(phone2.display_info())
print(phone2.take_photo())
print(phone2.make_call("987-654-3210"))


#Activity 2

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

def demonstrate_polymorphism():
    vehicles = [Car(), Plane(), Boat()]
    for vehicle in vehicles:
        print(vehicle.move())

demonstrate_polymorphism()
