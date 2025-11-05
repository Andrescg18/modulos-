
console.log("==========================")
console.log("BIENVENIDO AL DIRECTORIO ")
console.log("==========================")

const fs = require('fs');

let directorio = [
  { nombre: 'Diego Sanchez', telefono: '3001234567', correo: 'andrea@example.com' },
  { nombre: 'Andres Guardia', telefono: '3109876543', correo: 'andres@example.com' },
  { nombre: 'Sebastian Borda', telefono: '3152223333', correo: 'maria@example.com' },
  { nombre: 'Luis Rodriguez', telefono: '3204443434', correo: 'luis@example.com' },
  { nombre: 'Carolina Torres', telefono: '3145551212', correo: 'carolina@example.com' },
  { nombre: 'Valentina Sanchez', telefono: '3145551212', correo: 'valentina@example.com' },
  { nombre: 'Jhosep Perez', telefono: '3105331212', correo: 'jhosep@example.com' },
  { nombre: 'David Camelo', telefono: '3115351212', correo: 'david@example.com' },
  { nombre: 'Mario Perez', telefono: '3024851212', correo: 'mario@example.com' },
  { nombre: 'Erwin Joya', telefono: '3149951212', correo: 'erwin@example.com' },
  { nombre: 'Carlos Castiblanco', telefono: '3015441212', correo: 'carlos@example.com' },
];


function listarContactos() {
  console.log('Directorio de contactos:');
  directorio.forEach((contacto, index) => {
    console.log(`${index + 1}. Nombre: ${contacto.nombre}`);
    console.log(`   Teléfono: ${contacto.telefono}`);
    console.log(`   Correo: ${contacto.correo}`);
    console.log('--------------------------');
  });
  guardarEnTxt();
}


function agregarContacto(nombre, telefono, correo) {
  directorio.push({ nombre, telefono, correo });
  console.log(` Contacto agregado: ${nombre}`);
  guardarEnTxt();
}

function buscarContacto(nombre) {
  const resultado = directorio.find(c => c.nombre.toLowerCase() === nombre.toLowerCase());
  if (resultado) {
    console.log('Contacto encontrado:');
    console.log(resultado);
  } else {
    console.log(' Contacto no encontrado');
  }
}


function actualizarContacto(nombre, nuevoTelefono, nuevoCorreo) {
  const contacto = directorio.find(c => c.nombre.toLowerCase() === nombre.toLowerCase());
  if (contacto) {
    contacto.telefono = nuevoTelefono || contacto.telefono;
    contacto.correo = nuevoCorreo || contacto.correo;
    console.log(`Contacto actualizado: ${nombre}`);
    guardarEnTxt();
  } else {
    console.log(' No se encontró el contacto para actualizar');
  }
}

function eliminarContacto(nombre) {
  const index = directorio.findIndex(c => c.nombre.toLowerCase() === nombre.toLowerCase());
  if (index !== -1) {
    directorio.splice(index, 1);
    console.log(`Contacto eliminado: ${nombre}`);
    guardarEnTxt();
  } else {
    console.log(' No se encontró el contacto para eliminar');
  }
}

function guardarEnTxt() {
  let contenido = 'DIRECTORIO DE CONTACTOS\\n\\n';
  directorio.forEach((c, i) => {
    contenido += `${i + 1}. ${c.nombre}\\nTeléfono: ${c.telefono}\\nCorreo: ${c.correo}\\n--------------------------\\n`;
  });
  fs.writeFileSync('directorio.txt', contenido, 'utf8');
  console.log('Archivo directorio.txt actualizado');
}


listarContactos();
agregarContacto('Sofia Lopez', '3129998888', 'sofia@example.com');
buscarContacto('Luis Rodriguez');
actualizarContacto('Jhosep Perez', '3100000000', 'jhosep.new@example.com');
eliminarContacto('Mario Perez');
listarContactos();

module.exports={ 
    mensaje:"este archivo se ejecuto"
}