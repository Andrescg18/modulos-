// Ejercicio 40 - Mini CRUD en Memoria
// Descripción: Simula operaciones CRUD sobre lista en memoria.
// Archivo: ejercicio40.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

const db = []; function create(item){item.id=Date.now(); db.push(item); return item;} function read(id){return db.find(x=>x.id===id);} function update(id,changes){const it=read(id); if(it) Object.assign(it,changes); return it;} function remove(id){const i=db.findIndex(x=>x.id===id); if(i>=0) return db.splice(i,1)[0];}
const r = create({nombre:"Lote1"}); console.log("creado",r); update(r.id,{nombre:"Lote A"}); console.log("leido",read(r.id)); remove(r.id); console.log("db",db);
