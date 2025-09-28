// Ejemplo 57: Diccionario de futbol
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Futbol especial",
    tipo: "futbol",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
