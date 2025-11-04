// Ejercicio 27 - Generador de Fibonacci
// Descripción: Generator que produce la serie Fibonacci.
// Archivo: ejercicio27.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

function* fib(){
  let a=0,b=1;
  while(true){
    yield a; [a,b]=[b,a+b];
  }
}
const g = fib();
console.log(g.next().value, g.next().value, g.next().value, g.next().value);
