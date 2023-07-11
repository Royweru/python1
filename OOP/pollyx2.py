class Car:
    def __init__(self, make, model, ):
        self.make = make
        self.model = model

    def move(self):
        print('Driving around')


class Plane:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print('flying')


class MotorBike:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print('Ride around')


# instance of our class
car = Car('Toyota', 'Mark')
plane = Plane('Boeing', '737')
bike = MotorBike('Kawasaki', 'Ninja650')

for i in (car, plane, bike):
    i.move()
