function adapteeShipping() {
  this.request = function(origen, destino, peso){
    this.origen = origen
    this.destino = destino
    this.peso = peso
    this.total = Math.round(Math.random()*1000)

    return this.total
  }
}

function targetShipping() {

}
