// Ejemplo 73: Diccionario de caballos
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Caballos especial",
    tipo: "caballos",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
