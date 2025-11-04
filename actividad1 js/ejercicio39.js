// Ejercicio 39 - Simular Login Simple
// Descripción: Verifica credenciales en un array de usuarios.
// Archivo: ejercicio39.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

const usuarios=[{u:"admin",p:"1234"},{u:"juan",p:"abcd"}];
function login(user,pass){return usuarios.some(x=>x.u===user && x.p===pass);} 
console.log(login("juan","abcd"));
