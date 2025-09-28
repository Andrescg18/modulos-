// Ejemplo 49: Diccionario de misiones
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Misiones especial",
    tipo: "misiones",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
