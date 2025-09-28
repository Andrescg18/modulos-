// Ejemplo 17: Diccionario de paises
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Paises especial",
    tipo: "paises",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
