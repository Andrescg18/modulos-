// Ejemplo 33: Diccionario de empresas
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Empresas especial",
    tipo: "empresas",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
