# Patrones de Comportamiento
# ¿Como interactuo entre objetos?

### Chain of responsability
* Una manera de pasar una petición a una cadena de objetos (por ejemplo una solicitud de credito[Pasa por info respecto del cliente, info respecto del credito, luego si tengo acreedores, etc...]) [Acciones dentro de los metodos]

### Command
* Encapsular una petición de comandos como un objetos (Implementar diferentes ordenes o peticiones)[Accion encapsulada dentro de una clase]

### Interpreter
* Una manera de incluir elementos del lenguaje en un programa (se define una gramatica(estructura) y valida si se cumple para que se vaya ejecutando cada petición que la cumpla)

### Iterator
* Acceso secuencial a los elementos de una colección

### Mediator
* Define una comunicación simplificada entre clases(Cuando queremos exponer o compartir partes de nuestros servicios en  una APIs)

### Memento
* Captura y restaura el estado interno de un objetos(volver a un punto de ejecución)

### Observer
* Una forma de notificar cambios a varias clases

### State
* Altera el comportamiento de un objeto cuando cambia de estado

### Strategy
* Encapsula un algoritmo dentro de una clases

### Template Method
* Difiere los pasos exactos de un algoritmo a una subclase

### Visitor
* Define una nueva operación a una clase sin cambiarla
