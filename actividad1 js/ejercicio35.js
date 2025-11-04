// Ejercicio 35 - Throttle Simple
// Descripción: Implementa throttle para limitar ejecución.
// Archivo: ejercicio35.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

function throttle(fn, limit){let inThrottle=false; return function(...a){ if(!inThrottle){fn.apply(this,a); inThrottle=true; setTimeout(()=>inThrottle=false,limit);} };}
const tfn = throttle((m)=>console.log("Throttled",m),500);
tfn(1); tfn(2); setTimeout(()=>tfn(3),600);
