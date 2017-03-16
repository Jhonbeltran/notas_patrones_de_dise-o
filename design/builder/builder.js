function testBuilderPattern() {
  var shop = new Director()
  var carBuilder = null
  var car = shop.construct(carBuilder)

  car.doSomething()
}

function Director() {
  this.construct = function(builder){
    builder.step1()
    builder.step2()

    return builder.get()
  }
}
