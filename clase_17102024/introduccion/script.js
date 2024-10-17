document.title = 'Iniciar Sesion';
//--------------------------------------------------------------

// Crear el contenedor principal para el formulario
const container = document.createElement('div');
container.style.margin = '20px';

// Crear título
const title = document.createElement('h2');
title.textContent = 'Iniciar Sesion';
container.appendChild(title);

// Crear el formulario
const form = document.createElement('form');

// Crear campo de nombre de usuario
const usernamelabel = document.createElement('label');
usernamelabel.textContent = 'Nombre de Usuario';
const usernameInput = document.createElement('input');
usernameInput.type = 'text';
usernameInput.required = true;
form.appendChild(usernamelabel);
form.appendChild(usernameInput);

//--------------------------------------------------------------
// Crear campo de contraseña del usuario
const passwordlabel = document.createElement('label');
passwordlabel.textContent = 'Contraseña';
const passwordInput = document.createElement('input');
passwordInput.type = 'password'; // Asegúrate de que este tipo sea 'password'
passwordInput.required = true;
form.appendChild(passwordlabel);
form.appendChild(passwordInput);

// Crear botón de envío
const submitButton = document.createElement('button');
submitButton.textContent = 'Iniciar Sesion';
submitButton.type = 'submit';
form.appendChild(submitButton);

// Mensaje de respuesta
const message = document.createElement('p');
container.appendChild(form);
container.appendChild(message);

// Agregar el contenedor al cuerpo del documento
document.body.appendChild(container);

//DATOS DE INICIO DE SESION PREDEFINIDA

const validaUser= 'thigref';
const validaPassword = 'gemita';

//validar el nombre y el password
form.addEventListener('submit',(event)=> {
    event.preventDefault();

    //validar el nombre y el password
    if(validaUser && passwordInput.value == validaPassword){
        message.textContent = 'Bienvenido';
        message.style.color = 'green';
    }else{
        message.textContent = 'Nombre de usuario o contraseña incorrecto'
        message.style.color = 'red';
    }
    //limpiar los imputs
    usernameInput.value = '';
    passwordInput.value = '';
});

