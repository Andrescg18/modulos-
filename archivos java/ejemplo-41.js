// Ejemplo 41: Diccionario de libros
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Libros especial",
    tipo: "libros",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
