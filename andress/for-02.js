for (let carros = 0; carros <= 120; carros += 30) {
    if (carros > 100) {
        console.log(carros + " carros → tiene una flota de lujo");
    } else if (carros < 10) {
        console.log(carros + " carros → tiene buen gusto");
    } else {
        console.log(carros + " carros → tiene varios carros");
    }
}
