class cars:
    #properties of a car
    fuel = 'gasoline'
    def __init__(self, max_speed, time):
        print(f"This prints the car speed. Speed = {max_speed}")
        self.maxSpeed = max_speed
        self.time = time
    def calcDistance(self):
        print("Distance:")
        return self.maxSpeed * self.time

object1 = cars(90, 12) #initiating an object
print(object1.calcDistance())
print(type(object1))
print(type(object1.calcDistance()))
#ob2 = cars(45, 6)
''' print(object1.fuel, object1.maxSpeed, object1.time)
print(ob2.fuel)
 '''

