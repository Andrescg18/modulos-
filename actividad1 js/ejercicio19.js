// Ejercicio 19 - Destructuring de Objeto
// Descripción: Extrae propiedades con destructuring.
// Archivo: ejercicio19.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

const finca = {nombre: "La Esperanza", propietario: "Luis", area: 25};
const {nombre, area} = finca;
console.log(`${nombre} tiene ${area} ha`);
