
let colaClientes = ["Cliente A","Cliente B","Cliente C"];
console.log("Cola inicial:", colaClientes);
let atendido = colaClientes.shift();
console.log("Cliente atendido:", atendido);
colaClientes.unshift("Cliente Prioritario");
console.log("Cola final:", colaClientes);
