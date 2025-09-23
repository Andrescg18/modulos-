for (let camionetas = 0; camionetas <= 25; camionetas += 5) {
    if (camionetas > 20) {
        console.log(camionetas + " camionetas → es dueño de una empresa");
    } else if (camionetas < 5) {
        console.log(camionetas + " camionetas → tiene buen poder adquisitivo");
    } else {
        console.log(camionetas + " camionetas → es trabajador independiente");
    }
}
