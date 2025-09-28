// Ejemplo 65: Diccionario de espacio
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Espacio especial",
    tipo: "espacio",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
