class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed 
        self.mileage = mileage 

class Bus(vehicle):
    pass 

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle name: {}. Speed: {}. Mileage: {}").format(School_bus.name, School_bus.max_speed, School_bus.mileage)

