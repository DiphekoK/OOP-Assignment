# 🏗️ Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.__battery_life = battery_life  # Encapsulated attribute (private)

    def get_battery_life(self):
        return f"Battery life: {self.__battery_life} hours"

    def specs(self):
        return f"{self.brand} {self.model} - {self.__battery_life} hours battery"

# 🏗️ Inherited class: GamingSmartphone (Polymorphism)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, gpu):
        super().__init__(brand, model, battery_life)
        self.gpu = gpu

    def specs(self):
        return f"{self.brand} {self.model} (Gaming Edition) - GPU: {self.gpu}"

# Creating objects
phone1 = Smartphone("Apple", "iPhone 15", 20)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 24, "Adreno")

print(phone1.specs())  # Standard specs
print(phone1.get_battery_life())  # Access encapsulated attribute via method
print(gaming_phone.specs())  # Polymorphic method override
