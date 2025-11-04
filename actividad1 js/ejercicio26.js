// Ejercicio 26 - Async/Await con Fetch Simulado
// Descripción: Simula fetch con async/await y promesa.
// Archivo: ejercicio26.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

async function obtenerSimulado(){
  const datos = await new Promise(r=>setTimeout(()=>r({ok:true, datos:[1,2,3]}),300));
  if(datos.ok) console.log("Datos recibidos:", datos.datos);
}
obtenerSimulado();
