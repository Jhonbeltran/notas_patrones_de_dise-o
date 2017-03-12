## Síntomas de un mal diseño (En cuanto a programación orientada a objetos)

* Rigidez (Difícil de cambiar)
* Fragilidad (Cambiar algo y dañar otra cosa [Efecto dominó])
* Inmovilidad (No se pueden reutilizar modulos)
* Viscosidad (Realizar cambios impacta la forma en la que se diseña)

## Principios SOLID DE DOO

* Responsabilidad única
* Pincipio de abierto/cerrado (deben ser extensibles pero tambien deben ser cerradas para que no se modifiquen[Herencia adecuada])
* El principio de sustitución de Liskov (Clases que pueden ser sustituibles por la clase base[Interacción reutilizable])
* Principio de segregación de interfaces (Interfaces detalladas para cada cliente [vistas que se adaptan])
* Principio de inversión de dependencia (depender a abstracciónes y no de clases derivadas)

# Categorias y clasificacion de Patrones de Diseño (POSA [pattern oriented software architecture])

### Patrones de Arquitectura (descomponer en subsitemas, dar responsabilidades y generar comunicación)
* Ejemplos: Layers, MVC (Model, View, Controller), EDA (Event Driven Architecture), etc.

### Patrones de Diseño (Nivel especializado, como se implementa cada modulo[Comunicación de clases])
* Ejemplos: Factory Method, Facade, Strategy, Observer, etc

### Idioms/Modismos
* Ejemplo: Manejo de memoria, uso del lenguaje, convenciones de nombrado (tipado tipo pato), etc

# Categorias y clasificacion de Patrones de Diseño (GOF [gang of four])

### Proposito(Refleja lo que hace un patrón)
* Patrones de creacion, estructura(componer clases u objetos para construir objetos complejos) y comportamiento(interacción)

### Alcance(Patrones principalmene hacia clases u objetos)
[Objeto = instancia de una clase]
* Patrones de clase (Establece relaciones entre clases y subclases, interacción)
* Patrones de objetos (interacciónes entre objetos vivos [dinamicos])
