
const TASA_IMPUESTO = 0.15;
let precioString = prompt("Ingrese el precio:");
let precio = Number(precioString);
if (!isNaN(precio)) {
  let impuesto = precio * TASA_IMPUESTO;
  let total = precio + impuesto;
  console.log("Precio base:", precio.toFixed(2));
  console.log("Impuesto (15%):", impuesto.toFixed(2));
  console.log("Total a pagar:", total.toFixed(2));
  alert(`Total a pagar: ${total.toFixed(2)}`);
} else {
  console.log("Error: Entrada inválida");
  alert("Error: Entrada inválida");
}
