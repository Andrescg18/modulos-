// Ejemplo 85: Diccionario de meses
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Meses especial",
    tipo: "meses",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
