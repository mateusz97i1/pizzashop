let burgerBtn= document.querySelector('.burger-MENU');

let isBurgerOpen=false;

burgerBtn.onclick= function(){

    if(!isBurgerOpen){
        burgerBtn.style.backgroundPosition="center left 50px,center";
        isBurgerOpen=true;
    }

    
    else if(isBurgerOpen){
        burgerBtn.style.backgroundPosition="center,center left 50px";
         isBurgerOpen=false;
    }
   
}

