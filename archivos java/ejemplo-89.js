// Ejemplo 89: Diccionario de abuelos
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Abuelos especial",
    tipo: "abuelos",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
