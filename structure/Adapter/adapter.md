# Patrón: Adapter
# (a.k.a Wrapper)

### Problema
* Desea utilizar una clase existente, y su interfaz no coincide con la que necesita(ejemplo de los enchufes en america y en europa)
* desea crear clases reutilizables que cooperen con clases sin relación o imprevistas

### Contexto
* Relacionar dos componentes que no tiene una interfaz común

### Solución
* Convertir la interfaz de una clase en otra interfaz que el cliente espera

# Participantes

### Target
* Define la interfaz de dominio específico que utiliza el Client (toma de corriente)

### Adapter
* Adapta a la interfaz Adaptee para la interfaz de destino

### Adaptee
* Define una interfaz existente que necesita adapterse (conector)

### Client
* Colabora con objetos de acuerdo con la interfaz Target (persona)
