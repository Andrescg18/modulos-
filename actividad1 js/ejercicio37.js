// Ejercicio 37 - Contador con Closure
// Descripción: Crea contador usando closure (función que recuerda estado).
// Archivo: ejercicio37.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

function crearContador(init=0){let c=init; return {inc:()=>++c, dec:()=>--c, valor:()=>c};}
const ct = crearContador(5); console.log(ct.inc(), ct.inc(), ct.valor());
