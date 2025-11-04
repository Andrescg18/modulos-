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

function generarFacturaTXT() {
    let subtotal = 0;
    let contenido = "--------------FACTURA DE COMPRA-------------\n-------------------------\n";

    productos.forEach((p) => {
        contenido += `${p.nombre} - $${p.precio}\n`;
        subtotal += p.precio;
    });

    let valorIVA = subtotal * IVA;
    let total = subtotal + valorIVA;

    contenido += "-------------------------\n";
    contenido += `Subtotal: $${subtotal}\n`;
    contenido += `IVA (19%): $${valorIVA}\n`;
    contenido += `TOTAL A PAGAR: $${total}\n`;
    contenido += "-------------------------\n------------Gracias por su compra---------\n";

    fs.writeFileSync("factura.txt", contenido);
    console.log("Archivo factura.txt generado");
}

generarFacturaTXT();