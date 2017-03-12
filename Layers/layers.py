# Ejemplo de patrón arquitectónico 
#en una estructura cliente-servidor 

class CapaDePresentacion:
    def __init__(self):
        self.nombre = 'Capa de Presentación (Interfaz de usuario)'

    def delegaTareasA(self, delegaTareasA):
        self.delegaTareasA = delegaTareasA

    def servicioCapa3(self, parametro):
        print('Entramos al servicio %s' % self.nombre)
        self.delegaTareasA.servicioCapa2(parametro)
        print('Termina servicio %s' % self.nombre)


class CapaDeLogica:
    def __init__(self):
        self.nombre = 'Capa de Lógica (Procesamiento de la información)'

    def delegaTareasA(self, delegaTareasA):
        self.delegaTareasA = delegaTareasA

    def servicioCapa2(self, parametro):
        print('Entramos al servicio %s' % self.nombre)
        self.delegaTareasA.servicioCapa1(parametro)
        print('Termina servicio %s' % self.nombre)


class CapaDeAlmacenamientoDeDatos:
    def __init__(self):
        self.nombre = 'Capa De Almacenamiento De Datos'

    def servicioCapa1(self, parametro):
        print('Entramos al servicio %s' % self.nombre)
        print('Almacenamos el dato %s' % parametro)


if __name__ == '__main__':
    
    interfaz_de_usuario = CapaDePresentacion()
    logica_de_la_aplicacion = CapaDeLogica()
    almacenamiento_de_datos = CapaDeAlmacenamientoDeDatos()

    interfaz_de_usuario.delegaTareasA(logica_de_la_aplicacion)
    logica_de_la_aplicacion.delegaTareasA(almacenamiento_de_datos)

    interfaz_de_usuario.servicioCapa3('Parametro a almacenar')