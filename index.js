window.onload = () => {
    console.info('hi');
    background = document.getElementById("background");
    background.height = window.innerHeight;
    background.width = window.innerWidth;


};

window.onresize = () => {
    background.height = window.innerHeight;
    background.width = window.innerWidth;
}