var singleton = (function(){
  var instance;

  function init(){
    function privateMethod(){
      console.log("Private Method")
    }

    var privateNumber = Math.round(Math.random()*1000)

    return {
      publicMethod: function(){
        console.log("Entering Public Method");
        privateMethod()
        console.log("Exiting Public Method");
      },
      getRandomNumber: function(){
        return privateNumber;
      }
    }
  }

  return {
    getInstance : function(){
      if(!instance){
        instance = init()
      }
      return instance
    }
  }
})()


var testOne = singleton.getInstance()
testOne.publicMethod()

var testTwo = singleton.getInstance()
testTwo.publicMethod()

//True
console.log(testTwo.getRandomNumber() === testOne.getRandomNumber());
