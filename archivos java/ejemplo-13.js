// Ejemplo 13: Diccionario de canciones
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Canciones especial",
    tipo: "canciones",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
