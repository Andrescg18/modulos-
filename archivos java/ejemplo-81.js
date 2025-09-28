// Ejemplo 81: Diccionario de climas
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Climas especial",
    tipo: "climas",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
