// Ejemplo 61: Diccionario de planetas
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Planetas especial",
    tipo: "planetas",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
