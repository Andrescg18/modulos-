// Ejemplo 29: Diccionario de helados
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Helados especial",
    tipo: "helados",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
