
class Device:
    def __init__(self, brand):
        self.brand = brand   

    def info(self):
        print(f"This is a device from {self.brand}")

(Inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, storage):
        super().__init__(brand)  
        self.model = model        
        self.storage = storage    

    def call(self, number):
        print(f"📞 Calling {number} from {self.model}")

    def take_photo(self):
        print(f"📸 {self.model} takes a photo!")

 (Objects) 
phone1 = Smartphone("Apple", "iPhone 15", "256GB")
phone2 = Smartphone("Samsung", "Galaxy S24", "512GB")


phone1.info()          
phone1.call("123456")
phone2.take_photo()

