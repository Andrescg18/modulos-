// Ejemplo 5: Diccionario de numeros
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Numeros especial",
    tipo: "numeros",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
