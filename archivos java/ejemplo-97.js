// Ejemplo 97: Diccionario de algebra
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Algebra especial",
    tipo: "algebra",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
