// Ejemplo 21: Diccionario de autos
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Autos especial",
    tipo: "autos",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
