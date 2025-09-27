function calculadora_Basica() {
  let a = 12;  
  let b = 4;   

  return {
    suma: a + b,
    resta: a - b,
    multiplicacion: a * b,
    division: b === 0 ? "Error: división por cero" : a / b
  };
}


let resultado = calculadora_Basica();

console.log("Resultados de la calculadora básica:");
for (let operacion in resultado) {s
  console.log(`{operacion}: {resultado[operacion]}`);
}