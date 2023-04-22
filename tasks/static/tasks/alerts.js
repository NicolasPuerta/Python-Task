let message = document.querySelector(".warning");
let contador = 0;

let deletex = () => {
    message.remove(this);
    clearInterval(interval);
} 

let eraser = () => {
    contador++;
    if(contador == 5){ 
        deletex();
    }
    message.onclick = deletex;
}

let interval = setInterval(eraser,1000);