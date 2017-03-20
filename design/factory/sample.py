class MySimpleClass:
    def __init__(self):
        self.details = None
        print ('Init MySimpleClass')

    def getDetails(self):
        return self.details

class MyDerivedClass(MySimpleClass):
    def __init__(self):
        self.details = "An object of MyDerivedClass"


# Execute if this file is run as a script and not imported as a module
if __name__ == '__main__':
    print('Hola Mundo!')
    print('Hurra', 'Mi primer ejemplo en Python')
    a = MyDerivedClass()
    print(type(a))
    print( isinstance(a, MySimpleClass))
    print( isinstance(a, MyDerivedClass))
