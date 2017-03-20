# Patrón: Factory Method
## (a.k.a Virtual Constructor)
>

### Problema:
* Una clase no puede anticipar la clase de objetos que debe crear: porque dinamicamente se va a invocar (si llego a una pizzeria y pido una pizza hawaiana en ese momento la pizza se construye y se genera).

* Una clase quiere que sus subclases especifiquen los objetos que crean.

### Contexto
* Los Frameworks utilizan clases abstractas para definir y mantener las relaciones dentra objetos. Una responsabilidad es crear tales objetos.

### Solución
* Definir una interfaz para crear un objeto, pero dejando la elección de su tipo a las subclases, la creación se aplaza hasta el tiempo de ejecución.


# Participantes

### Product

* Define la interfaz para los objetos que FactoryMethod crea. (Carro)

### ConcreteProduct

* Implementa la interfaz Product (Carro [Deportivo])

### Creator(Factory)

* Declara el método FactoryMethod, que devuelve un objeto Producto. Puede llamar al método de generación para la creación de objetos Product (Constructor)

### ConcreteCreator

* Sobreescribe el metodo de generación para crear objetos ConcreteProduct (El constructor que genera el tipo de objeto concreto)
