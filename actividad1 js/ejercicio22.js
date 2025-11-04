// Ejercicio 22 - Contar Palabras
// Descripción: Cuenta cuántas palabras tiene una frase.
// Archivo: ejercicio22.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

const frase = "La cosecha será abundante este año";
const palabras = frase.trim().split(/\s+/).length;
console.log("Palabras:", palabras);
