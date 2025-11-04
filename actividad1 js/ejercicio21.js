// Ejercicio 21 - Validar Email Simple
// Descripción: Función que valida estructura básica de email.
// Archivo: ejercicio21.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

function validarEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}
console.log(validarEmail("usuario@ejemplo.com"));
