//Adaptee
function adapteeShipping() {
  this.request = function(origen, destino, peso){
    this.origen = origen
    this.destino = destino
    this.peso = peso
    // this.total = Math.round(Math.random()*1000)
    this.total = peso * 100


    return this.total
  }
}

//Target
function targetShipping() {
  this.login = function(credentials){
    //TO DO
  }
  this.setOrigen = function(origen){
    this.origen = origen
  }
  this.setDestino = function(destino){
    this.destino = destino
  }

  this.calculate = function(peso){
    this.peso = peso
    // this.total = Math.round(Math.random()*1000)
    this.total = peso * 200

    return this.total
  }
}

//Adapter
function shippingAdapter(credentials) {
  var target = new targetShipping()

  target.login()

  return {
    request : function(origen, destino, peso){
      target.setOrigen(origen)
      target.setDestino(destino)

      return target.calculate(peso)
    }
  }
}

function client() {
  this.run = function() {
    var oldInterface = new adapteeShipping();
    var cost = oldInterface.request('1234', '321', 56)
    console.log(cost);

    var credenciales = 'user/pass'
    var adapter = shippingAdapter(credenciales)

    var newCost = adapter.request('1234', '321', 56)

    console.log(newCost);

  }
}

cliente = new client()
cliente.run()
