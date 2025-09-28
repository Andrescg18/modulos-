// Ejemplo 69: Diccionario de rios
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Rios especial",
    tipo: "rios",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
