var yPos = window.pageYOffset;

const navHeight = document.querySelector('.nav-container').offsetHeight;
console.log(navHeight)
window.onscroll = function() {
        var xPos = window.innerWidth;
        if(xPos>425){
            var currentPos = window.pageYOffset;
            if (yPos > currentPos) document.querySelector('.nav-container').style.top = "0";
            else document.querySelector('.nav-container').style.top = `-${navHeight}px`;
            yPos = currentPos; 
        }
        else document.querySelector('.nav-container').style.top = "auto";
}