
function ejercicio01() {
  let numero1 = prompt("Ingrese el primer número:");
  let numero2 = prompt("Ingrese el segundo número:");
  let n1 = parseInt(numero1, 10);
  let n2 = parseInt(numero2, 10);
  if (isNaN(n1) || isNaN(n2)) {
    alert("Por favor ingrese números válidos");
    return;
  }
  let suma = n1 + n2;
  alert(`El resultado de ${n1} + ${n2} = ${suma}`);
}
ejercicio01();
