class PresentationLayer:
    def __init__(self):
        self.name = 'PresentationLayer'

    def setLowerLayer(self, lowerLayer):
        self.lowerLayer = lowerLayer

    def layerService3(self, param):
        print('Entramos al servicio %s' % self.name)
        self.lowerLayer.layerService2(param)
        print('Termina servicio %s' % self.name)


class LogicLayer:
    def __init__(self):
        self.name = 'LogicLayer'

    def setLowerLayer(self, lowerLayer):
        self.lowerLayer = lowerLayer

    def layerService2(self, param):
        print('Entramos al servicio %s' % self.name)
        self.lowerLayer.layerService1(param)
        print('Termina servicio %s' % self.name)


class DataLayer:
    def __init__(self):
        self.name = 'DataLayer'

    def layerService1(self, param):
        print('Entramos al servicio %s' % self.name)
        print('Ejecutamos con %s' % param)


if __name__ == '__main__':
    
    ui = PresentationLayer()
    logic = LogicLayer()
    data = DataLayer()

    ui.setLowerLayer(logic)
    logic.setLowerLayer(data)

    ui.layerService3('exampleParam')