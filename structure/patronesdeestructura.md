# Patrones de estructura
## ¿Cómo pueden trabajar una clase y un objeto?
## Nos ayudan a trabajar la comunicación de clases y objetos

### Adapter (wrapper)
* Relaciona interfaces de diferentes clases (conectar dos modulos o sistemas construidos en momentos diferentes o con intensiones diferentes pero que actualemente necesitan unirse para apoyar la construcción de uno de ellos)

### Bridge
* Separa la interfaz de un objeto de su implementación (consumo de APIs)

### Composite
* Una estructura de árbol de objetos simples y compuestos (comunicación entre nodos)

### Decorador
* Añadir responsabilidades a los objetos dinámicamente (permisos para acceder a ciertos datos, nos apoyamos en un securityManager (AuthLogin) y la decoración para cada usuario)

### Facade
* Una única clase que representa todo un subsistema (diferentes piezas o subsistemas complejos y queremos minimizar la comunicacion con otros subsistemas)

### Flyweight
* Una instancia usada para compartir eficientemente

### Proxy
* Un objeto que representa a otro objeto
* Intermedio entre el objeto y el cliente final
