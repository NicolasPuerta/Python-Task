const hamburger = document.querySelector(".hamburger");
hamburger.onclick = function(){
    navbar = document.querySelector(".nav-bar");
    navbar.classList.toggle("active");
}