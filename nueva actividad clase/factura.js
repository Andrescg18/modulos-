
const fs = require('fs');

let productos = [
  { nombre: "huevos", precio: 5000 },
  { nombre: "carne", precio: 8000 },
  { nombre: "pollo", precio: 12000 },
  { nombre: "pescado", precio: 3000 },
  { nombre: "leche", precio: 15000 },
  { nombre: "aceite", precio: 7000 },
  { nombre: "arroz", precio: 9500 },
  { nombre: "granos", precio: 10000 },
  { nombre: "espaguettis", precio: 6000 },
  { nombre: "gaseosa", precio: 20000 }
];

const IVA = 0.19;


function agregarProducto(nombre, precio) {
  productos.push({ nombre, precio });
  console.log(` Producto agregado: ${nombre} - $${precio}`);
  generarFacturaTXT();
}


function listarProductos() {
  console.log("Lista de productos:");
  productos.forEach((p, i) => console.log(`${i + 1}. ${p.nombre} - $${p.precio}`));
}


function actualizarProducto(nombre, nuevoPrecio) {
  const producto = productos.find(p => p.nombre.toLowerCase() === nombre.toLowerCase());
  if (producto) {
    producto.precio = nuevoPrecio;
    console.log(`Producto actualizado: ${nombre} ahora cuesta $${nuevoPrecio}`);
    generarFacturaTXT();
  } else {
    console.log("Producto no encontrado");
  }
}


function eliminarProducto(nombre) {
  const index = productos.findIndex(p => p.nombre.toLowerCase() === nombre.toLowerCase());
  if (index !== -1) {
    productos.splice(index, 1);
    console.log(`Producto eliminado: ${nombre}`);
    generarFacturaTXT();
  } else {
    console.log(" no encontrado para eliminar");
  }
}


function generarFacturaTXT() {
  let subtotal = 0;
  let contenido = "--------------FACTURA DE COMPRA-------------\n";
  contenido += "=============================================\n";

  productos.forEach((p) => {
    contenido += `${p.nombre} - $${p.precio}\n`;
    subtotal += p.precio;
  });

  let valorIVA = subtotal * IVA;
  let total = subtotal + valorIVA;

  contenido += "=============================================\n";
  contenido += `Subtotal: $${subtotal}\n`;
  contenido += `IVA (19%): $${valorIVA}\n`;
  contenido += `TOTAL A PAGAR: $${total}\n`;
  contenido += "=============================================\n";
  contenido += "--------- ¡Gracias por su compra! -----------\n";

  fs.writeFileSync("factura.txt", contenido);
  console.log("Archivo factura.txt actualizado");
}


listarProductos();

console.log("\\n--- Agregando producto ---");
agregarProducto("pan", 2500);

console.log("\\n--- Actualizando producto ---");
actualizarProducto("carne", 9000);

console.log("\\n--- Eliminando producto ---");
eliminarProducto("aceite");

console.log("\\n--- Lista final ---");
listarProductos();

console.log("\\n--- Factura actualizada ---");
generarFacturaTXT();
