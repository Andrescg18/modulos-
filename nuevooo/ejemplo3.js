const fs = require('fs');
const archivo_datos= "datos.txt";
fs.readFile (archivo_datos, 'UTF8'
    (err,data) => {

 console.log (data);   }
)