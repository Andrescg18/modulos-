// Ejemplo 1: Diccionario de frutas
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Frutas especial",
    tipo: "frutas",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
