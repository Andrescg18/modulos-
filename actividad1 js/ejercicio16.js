// Ejercicio 16 - Reducir para Sumar
// Descripción: Suma todos los elementos de un array con reduce.
// Archivo: ejercicio16.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

const valores = [10, 20, 5, 15];
const total = valores.reduce((acc, cur) => acc + cur, 0);
console.log("Total:", total);
