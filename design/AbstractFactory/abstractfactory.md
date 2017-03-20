# Patrón: AbstractFactory Method
# (a.k.a Kit)

### Problema
* Desea proporcionar una biblioteca de clases de productos
* Desea revelar sólo sus interfaces, no sus implementaciones

### Contexto
* Evitar añadir codigo a las clases existentes con el fin de hacer que se encapsule información mas general

### Solución
* Proporciona una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas
* Biblioteca de clases de productos (Familias de productos(objetos))

# Participantes

### AbstractFactory
* Declara una interfaz para las operaciones que crean AbstractProduct

### ConcreteFactory
* Implementa operaciones para crear Product concretos

### AbstractProduct
* Declara una interfaz para un tipo de objetos Product

### Product
* Define un producto a ser creado por el ConcreteFactory correspondiente; que implementa la interfaz AbstractProduct

### Client
* Utiliza las interfaces declaradas por las clases AbstractFactory y AbstractProduct
