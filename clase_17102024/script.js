document.title = 'clase de JS';
console.log(document.title);

const h1 = document.createElement("h1");
h1.textContent = "Mi texto desde JS";

document.body.appendChild(h1);

const parrafo = document.createElement("parrafo");
parrafo.textContent = "Mi texto desde JS";

document.body.appendChild(parrafo);
