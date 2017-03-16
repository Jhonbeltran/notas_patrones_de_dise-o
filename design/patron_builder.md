# Patrón Builder

### Problema:

* Entre mas compleja la apliación, mas complejos son los objetos y las clases que utilizamos en ella.

### Contexto:

* Apliación que necesita un mecanismo para construir objetos complejos y que a su vez sea independiente del objeto que lo construye.
(objetos complejos: atributos + objetos dentro de objetos )

### Solución:

* Definir una instancia para crear un objeto y dejar que las subsclases decidan cual objeto debe instanciar.


## Participantes del patrón Builder

### Builder (class)

* Interfaz (clase abstracta) identifica las partes del objeto complejo.

### ConcreteBuilder

* Herencia de diferentes tipos de builders.

### Director (class)

* Construye el objeto complejo usando el Builder Interfaz

### Product

* El objeto complejo que va a ser construido
