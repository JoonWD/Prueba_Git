let num = parseInt(prompt("Ingresa un número:")); 
let esPrimo = true; 

for (let i = 2; i < num; i++) {
    if (num % i === 0) {
        esPrimo = false; 
        break; 
    }
}

if (esPrimo) {
    console.log(num + " es un número primo."); 
} else {
    console.log(num + " no es un número primo.");
}
