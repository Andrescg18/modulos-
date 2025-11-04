// Ejercicio 25 - Promesa Simple
// Descripción: Crea y consume una promesa que se resuelve tras timeout.
// Archivo: ejercicio25.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

function esperar(ms){
  return new Promise(resolve => setTimeout(() => resolve(`Esperado ${ms}ms`), ms));
}
esperar(800).then(msg => console.log(msg));
