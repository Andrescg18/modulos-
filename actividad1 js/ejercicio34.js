// Ejercicio 34 - Debounce Simple
// Descripción: Implementa debounce para llamadas frecuentes.
// Archivo: ejercicio34.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

function debounce(fn, wait){let t; return function(...a){clearTimeout(t); t=setTimeout(()=>fn.apply(this,a),wait);};}
const f = debounce((msg)=>console.log("Debounced:",msg), 200);
f("x"); f("y"); setTimeout(()=>f("z"),300);
