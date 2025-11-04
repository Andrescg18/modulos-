// Ejercicio 38 - Validar Password Fuerte
// Descripción: Función que verifica condiciones básicas de contraseña.
// Archivo: ejercicio38.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

function fuerte(p){ return /[A-Z]/.test(p) && /[0-9]/.test(p) && p.length>=8; }
console.log(fuerte("MiPass123"));
