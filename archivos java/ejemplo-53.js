// Ejemplo 53: Diccionario de moviles
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Moviles especial",
    tipo: "moviles",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
