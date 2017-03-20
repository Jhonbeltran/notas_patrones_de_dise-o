from abc import ABCMeta

#interfaz
#así se declara una clase abstracta
#             vvvvvvvvvvv
class Car(metaclass=ABCMeta):
    def __init__(self):
        self.name = None
        self.maxSpeed = None


# ConcreteProduct
class SportsCar(Car):
    def __init__(self):
        self.name = 'Deportivo'
        self.maxSpeed = '250 km/h'

# ConcreteProduct
class FamilyCar(Car):
    def __init__(self):
        self.name = 'Familiar'
        self.maxSpeed = '150 km/h'

class MyFactory():
    def createCar(self, carType):
        self.car = None
        if carType == 'sports':
            self.car = SportsCar
            print('Car type {:s} generated'.format(carType))
        elif carType == 'family':
            self.car = FamilyCar
            print('Car type {:s} generated'.format(carType))
        else:
            print('Car type {:s} is not definded'.format(carType))

        return self.car

    def doSomething(self):
        print(self.car)

# Execute if this file is run as a script and not imported as a module
if __name__ == '__main__':
    factory = MyFactory()
    sport = factory.createCar('sports')
    family = factory.createCar('family')

    print(sport)
    print(family)
