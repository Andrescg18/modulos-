// Ejercicio 18 - Clonar Objeto (Spread)
// Descripción: Copia y modifica un objeto con spread operator.
// Archivo: ejercicio18.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

const origen = {cultivo: "maíz", hectareas: 10};
const copia = {...origen, hectareas: 12};
console.log(copia);
