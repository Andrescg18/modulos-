// Ejemplo 25: Diccionario de barcos
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Barcos especial",
    tipo: "barcos",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
