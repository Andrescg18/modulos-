
class AutoConVel {
  constructor(marca, velocidadInicial=0) {
    this.marca = marca;
    this._velocidad = velocidadInicial;
  }
  set velocidad(valor) {
    if (valor >= 0) this._velocidad = valor;
    else console.log("Error: Velocidad no puede ser negativa");
  }
  get velocidad() {
    return this._velocidad;
  }
}
const carro = new AutoConVel("Ford",80);
console.log("Velocidad:", carro.velocidad);
carro.velocidad = 120;
carro.velocidad = -50;
