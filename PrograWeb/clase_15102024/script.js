//definicion de una funcioin
/*
function hello(){
    console.log('Hola clase');
    console.log('5IV7');

}

//llamar a la funcion
hello();
hello();
hello();
hello();
hello();

*/



/*

//RETORNO DE UNA FUNCION
function hello(){
    return 'Hola clase'
}

const result =  hello()

console.log(result);

*/

//funcion que retorna otea funcion




/*
function hello(){
    return function (){
        return 'hola soy la funcion 2';
        
    }
}

console.log(hello()())

*/

/*
//funcion con parametros
function add(x,y){
    console.log(x+y)
}

add(5,10)



//control de error

function add(x,y=0){


    if {y===undefined}{
        y=0
    }
    console.log(x+y)
}

add(5,undefined)

*/

//parametro tipo cadena

/*

function add(name){
    console.log('hola'+name);
}

add("Clase js")

*/

//objetos

const user = {
    nombre: 'Alvarado',
    apellidoP: 'Reyes',
    apellidoM: 'Quiroz',
    edad: 91,
    direccion :{
        calle: 'Nicolas Bravo',
        no:598,
        colonia: 'Narvarte',
        delegacion: 'Los Pinos'
    },

    amigos: ['Raul', 'Maria'],
    activo: true

}

//consola nombre apellido paterno 
//alert activo;
//consola edad 
//alert calle no colonia delegacion
//consola amigos

function copi(){
    console.log(user.nombre+ ' ' + user.apellidoP + ' '+ user.apellidoM);
    console.log(user.edad);
    console.log(user.amigos);
}

copi()

alert('activo'+ ' ' + user.direccion.calle + ' ' + user.direccion.no + ' ' + user.direccion.colonia+ ' ' + user.direccion.delegacion)


