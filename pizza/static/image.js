let image1=document.querySelector('.imge02')
let arrowTrans=document.querySelector('.arrow')

let isArrowClicked=false;

arrowTrans.onclick=function(){
    if(!isArrowClicked){
        image1.classList.add('imge02Trans')
        arrowTrans.classList.add('arrowRotate')
        isArrowClicked=true;
    }
    else if(isArrowClicked){
        image1.classList.remove('imge02Trans')
        arrowTrans.classList.remove('arrowRotate')
        isArrowClicked=false;
    }

}