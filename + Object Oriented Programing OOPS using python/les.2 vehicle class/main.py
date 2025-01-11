class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


model = vehicle(240,18)        
print(f"Model Max speed: {model.max_speed}")
print(f"Model Mileage: {model.mileage}")
