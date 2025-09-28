// Ejemplo 77: Diccionario de traducciones
function mostrarObjeto() {
  let Andres_guardia = {
    nombre: "Traducciones especial",
    tipo: "traducciones",
    activo: true
  };

  for (let clave in Andres_guardia) {
    console.log(clave + ": " + Andres_guardia[clave]);
  }
}
mostrarObjeto();
