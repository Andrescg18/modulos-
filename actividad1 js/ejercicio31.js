// Ejercicio 31 - Merge de Arrays Unicos
// Descripción: Une arrays eliminando duplicados.
// Archivo: ejercicio31.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

const a=[1,2,3], b=[3,4,5];
const unico = [...new Set([...a,...b])];
console.log(unico);
