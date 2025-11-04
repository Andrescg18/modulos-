// Ejercicio 33 - Proxy para Validación
// Descripción: Usa Proxy para validar asignaciones en objeto.
// Archivo: ejercicio33.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

const meta = {nombre:"Finca", area:5};
const proxy = new Proxy(meta,{set(obj,prop,val){ if(prop==="area" && val<0) throw new Error("Area inválida"); obj[prop]=val; return true; }});
proxy.area = 8; console.log(proxy.area);
