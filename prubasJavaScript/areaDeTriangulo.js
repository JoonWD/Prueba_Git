function areaDeTriangulo() {
    let base = parseFloat(prompt("Ingrese la base del triángulo:"));
    let altura = parseFloat(prompt("Ingrese la altura del triángulo:"));
    
    if (isNaN(base) || isNaN(altura)) {
        console.log("Por favor, ingrese valores numéricos válidos.");
        return;
    }
    
    let area = (base * altura) / 2;
    alert("El área del triángulo es: " + area);
}