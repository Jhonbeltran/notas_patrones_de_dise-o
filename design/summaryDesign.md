# Algunas notas sobre Patrones de Creación

* Abstract Factory tiene el objeto factory produciendo objetos de varias clases

* Builder tiene el objeto factory construyendo un producto incrementalmente usando una estructura compleja

* Las clases AbstractFactory a menudo son implementadas usando FactoryMethods pero tambien pueden ser implementadas usando prototype.

* Builder se enfoca en construir objetos complejos paso a paso

* Abstract Factory hace énfasis en una familia de objetos producto(ya sean simples o complejos)

* Builder regresa el producto como un paso final, el Abstract Factory regresa el producto inmediatamente
