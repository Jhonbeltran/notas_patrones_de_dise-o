from abc import ABCMeta, abstractmethod

#interfaz
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

class Factory(metaclass=ABCMeta):
    def __init__(self):
        self.manufacturer = None

    #Esto obliga a la fabrica a implementar el metodo createCar
    @abstractmethod
    def createCar(self, carType):
        pass

    @staticmethod
    def get_factory(factoryName):
        if factoryName == 'Audi':
            return Audi()
        elif factoryName == 'Mazda':
            return Mazda()
        raise TypeError('Unknok Factory')

class Audi(Factory):
    def __init__(self):
        self.manufacturer = 'Audi'
        print('Factoy {:s} is generating your cars'.format(self.manufacturer))

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
    factory = Factory.get_factory('Audi')
    print (factory)

    sport = factory.createCar('sports')
    family = factory.createCar('family')

    print(sport)
    print(family)
