// Ejercicio 15 - Mapear Precios con IVA
// Descripción: Aplica IVA a precios usando map.
// Archivo: ejercicio15.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

const precios = [100, 250, 399];
const iva = 0.19;
const conIVA = precios.map(p => +(p * (1 + iva)).toFixed(2));
console.log(conIVA);
