// Ejercicio 24 - Comprobar Anagramas
// Descripción: Verifica si dos palabras son anagramas.
// Archivo: ejercicio24.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

function esAnagrama(a,b){
  const norm = s => s.replace(/[^a-z0-9]/gi,"").toLowerCase().split("").sort().join("");
  return norm(a) === norm(b);
}
console.log(esAnagrama("roma","amor"));
