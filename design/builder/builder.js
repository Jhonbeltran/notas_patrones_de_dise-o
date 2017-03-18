function testBuilderPattern() {
  console.log("||| REVISAREMOS COMO CONSTRUIMOS UN CARRO USANDO UN" +
              " PATRON BUILDER ||||");
  var shop = new Director()
  var carBuilder = new CarBuilder()
  var car = shop.construct(carBuilder)

  car.doSomething()
}

function Director() {
  console.log("El proceso inicia entrando al director de la construccion")
  this.construct = function(builder){
    console.log("Se inicia la construcción")
    builder.step1()
    builder.step2()

    return builder.getResult()
  }
}

function CarBuilder() {
  console.log("Se revisa que necesita para crearse el carro")
  this.car = null
  this.step1 = function() {
    console.log("Se ejecutan las actividades base para la creación")
    this.car = new Car();
  }
  this.step2 = function() {
    console.log("Se agregan las partes fundamentales del carro")
    this.car.addParts()
  }

  this.getResult = function(){
    console.log("Se tiene como resultado final el carro construido");
    return this.car
  }
}

function Car(){
  console.log("Inicia el proceso de ensamblado");
  this.doors = 0
  this.addParts = function() {
    console.log("Agregamos las puertas");
    this.doors = 4
  }

  this.doSomething = function() {
    console.log("Tenemos un carro con " + this.doors + " puertas");
  }
}


testBuilderPattern()
