var menuButton = document.getElementById('drop-menu');
var menu = document.querySelector('nav>ul');
var bar = document.getElementById("bar");
var close = document.querySelector('.status')

function showMenu(e){
    e.stopPropagation();
    if (menu.style.display == "none" || menu.style.display == ''){
        menu.style.display = "flex";
       bar.className = "fas fa-times fa-2x";
    }else{
        menu.style.display = "none";
        bar.className = "fas fa-bars fa-2x";
    }
};

menuButton.addEventListener("click", showMenu);