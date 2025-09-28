// Ejemplo 9: Diccionario de notas
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Notas especial",
    tipo: "notas",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
