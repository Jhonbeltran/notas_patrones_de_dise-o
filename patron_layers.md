# Patron Arquitectonico Layers


## Problema: 

* Se pueden identificar los modulos (cada uno de ellos no depende de otro)

* Comunicacion (peticiones) desde la capa superior a la inferior y respuestas en sentido inverso

## Contexto

* Apliacación grande que se requiere descomponer

## Solución

* Estructurar apliacion en grupos de sub tareas de tal manera que cada uno tenga un nivel de abstracción especial y que nos permita tener comunicación.

## Participantes del patrón Layers

### Participantes

Cada layer se puede ver como: 

- Clase: Layer J

- Colaborador: Layer J-1

- Responsabilidad: Proveer servicios usados por Layer J+1, delegar subtareas a Layer J-1



