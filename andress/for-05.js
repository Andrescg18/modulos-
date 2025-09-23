for (let barcos = 0; barcos <= 7; barcos++) {
    if (barcos > 5) {
        console.log(barcos + " barcos → es dueño de un puerto privado");
    } else if (barcos < 1) {
        console.log(barcos + " barcos → aún no navega");
    } else {
        console.log(barcos + " barcos → es aficionado a los yates");
    }
}
