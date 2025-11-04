const fs = require ('fs');
const archivo_datos = "datos.txt";
fs.writeFile(archivo_datos,"hola pablo",
    (err) => err? console.error (err):
    console.log ("archivo creado"));
   
    