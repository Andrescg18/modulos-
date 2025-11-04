// Ejercicio 23 - Generar ID Único
// Descripción: Genera un ID simple usando fecha y aleatorio.
// Archivo: ejercicio23.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

function generarId(prefijo="ID"){
  return `${prefijo}-${Date.now()}-${Math.floor(Math.random()*1000)}`;
}
console.log(generarId("COSE"));
