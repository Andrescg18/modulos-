for (let bicicletas = 0; bicicletas <= 15; bicicletas += 3) {
    if (bicicletas > 10) {
        console.log(bicicletas + " bicicletas → tiene una tienda de bicicletas");
    } else if (bicicletas < 2) {
        console.log(bicicletas + " bicicletas → usa bici solo para pasear");
    } else {
        console.log(bicicletas + " bicicletas → es fanático del ciclismo");
    }
}
