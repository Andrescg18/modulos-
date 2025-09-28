// Ejemplo 93: Diccionario de arte
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Arte especial",
    tipo: "arte",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
