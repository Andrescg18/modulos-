// Ejercicio 36 - Buscar Máximo y Mínimo
// Descripción: Devuelve max y min de un array en una pasada.
// Archivo: ejercicio36.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

function minMax(arr){let min=Infinity,max=-Infinity; for(const v of arr){ if(v<min) min=v; if(v>max) max=v;} return {min,max};}
console.log(minMax([5,3,9,1,6]));
