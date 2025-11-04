// Ejercicio 12 - Factorial Iterativo
// Descripción: Calcula factorial usando bucle for.
// Archivo: ejercicio12.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

function factorial(n) {
  if (n < 0) return null;
  let res = 1;
  for (let i = 2; i <= n; i++) res *= i;
  return res;
}
console.log("5! =", factorial(5));
