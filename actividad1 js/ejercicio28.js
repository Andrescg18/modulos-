// Ejercicio 28 - Memoización
// Descripción: Crea una función memoizada para fibonacci recursiva.
// Archivo: ejercicio28.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

function memoize(fn){
  const cache = new Map();
  return (...args)=>{
    const key = JSON.stringify(args);
    if(cache.has(key)) return cache.get(key);
    const res = fn(...args); cache.set(key,res); return res;
  }
}
const fibRec = memoize(function(n){ if(n<2) return n; return fibRec(n-1)+fibRec(n-2); });
console.log(fibRec(20));
