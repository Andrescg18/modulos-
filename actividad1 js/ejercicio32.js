// Ejercicio 32 - Clase Agricultor
// Descripción: Define clase y métodos básicos.
// Archivo: ejercicio32.js
// Autor: Andrés Camilo Guardia
// Idioma: Español

class Agricultor{constructor(nombre){this.nombre=nombre;this.cosechas=[];}registrar(c){this.cosechas.push(c);}resumen(){return `${this.nombre} - registros: ${this.cosechas.length}`}}
const ag=new Agricultor("Pedro");ag.registrar("maíz");console.log(ag.resumen());
