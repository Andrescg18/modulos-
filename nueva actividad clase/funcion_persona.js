function Persona(nombre, apellido, edad) {
  this.nombre = nombre;
  this.apellido = apellido;
  this.edad = edad;
}

Persona.prototype.saludar = function() {
  return `Hola como estan compañeros, soy andres ${this.nombre} ${this.apellido} y tengo ${this.edad} años.`;
};

const persona1 = new Persona("Andres", "Guardia", 19);
console.log(persona1.saludar());
