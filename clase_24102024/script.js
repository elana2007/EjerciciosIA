//arreglos 
/*
let array = ["dato1", 1, Boolean];

console.log("tamaño array: " + array.length); 

array.push("insert nuevo val"); console.log(array[3]); 

console.log("nuevo tamaño array: " + array.length); 
console.log(array[3]);
*/

//PRACTICA

let array = [];

for(i = 0;i <= 10; i++) {
    
    
    //defini
    let x = i * 5;


    array.push(x);

    console.log("5 " + "x " + i + " = " + array[i]);

    if(array.length >= 7){



        console.log("final")



        break;
    }
}
