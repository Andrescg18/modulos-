// Ejercicio 30 - Invertir Array sin reverse
// Descripción: Invierte un array manualmente.
// Archivo: ejercicio30.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

const arr = [1,2,3,4,5];
const inv = [];
for(let i=arr.length-1;i>=0;i--) inv.push(arr[i]);
console.log(inv);
