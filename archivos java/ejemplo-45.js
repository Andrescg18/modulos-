// Ejemplo 45: Diccionario de paginas
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Paginas especial",
    tipo: "paginas",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
