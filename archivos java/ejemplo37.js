// Ejemplo 37: Diccionario de precios
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Precios especial",
    tipo: "precios",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
