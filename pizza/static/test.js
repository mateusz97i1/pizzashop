let btnRed=document.querySelector(".btn01");
let btngreen=document.querySelector(".btn02");
let btnRestore=document.querySelector(".btn03");
let btnLightMode=document.querySelector(".changeBgc");
let squere=document.querySelector(".squere");
let mainBgc=document.querySelector('main')
let isbtnLightOpen=false;


function redColor(){
    squere.classList.add('red')
    squere.classList.remove('green')
}

function greenColor(){
    squere.classList.add('green')
    squere.classList.remove('red')
}

function rerestoreColor(){
    squere.classList.remove('red','green')

}

btnLightMode.onclick= function(){
    if(!isbtnLightOpen){
        mainBgc.classList.add('light')
        mainBgc.classList.remove('dark')
        isbtnLightOpen=true;
    }
    else if(isbtnLightOpen){
        mainBgc.classList.add('dark')
        mainBgc.classList.remove('light')
        isbtnLightOpen=false;
    }
}

btnRed.addEventListener("click",redColor)
btngreen.addEventListener("click",greenColor)
btnRestore.addEventListener("click",rerestoreColor)
btnLightMode.addEventListener("click",lightColor)

console.log(btnLightMode)