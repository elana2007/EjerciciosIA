//definimos funcion normal

function hola(a,b){
    return a+b;
}

console.log(hola(3,5));

// 1 convertir a funcion flecha

const suma = (a,b) => {
    return a+b;
}
console.log(suma(3,5));

//2 simplificar

const suma2 = (a,b) => a+b ; 
console.log(suma(5,5));

//04 con un parametro

const cuadrado = x => x*x;
console.log(cuadrado(50));

