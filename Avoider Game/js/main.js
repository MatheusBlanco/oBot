function drawAvatar(){
    var gameCanvas = document.getElementById("gameCanvas");
    var avatarImage = new Image();

    avatarImage.src = "img/avatar.png";
    gameCanvas.getContext("2d").drawImage(avatarImage, Math.random() * 100, Math.random() * 100);

    gameCanvas.addEventListener("mousemove", redrawAvatar);
}

function redrawAvatar(mouseEvent){
    var gameCanvas = document.getElementById("gameCanvas");
    var avatarImage = new Image();
    var enemyImage = new Image();
     
    avatarImage.src = "img/avatar.png";
    enemyImage.src = "img/enemy.png";
    gameCanvas.width = 400;
    gameCanvas.getContext("2d").drawImage(avatarImage, mouseEvent.offsetX, mouseEvent.offsetY);
    gameCanvas.getContext("2d").drawImage(enemyImage, 250, 150);

    if (mouseEvent.offsetX > 220 && mouseEvent.offsetX < 280 && mouseEvent.offsetY > 117 && mouseEvent.offsetY < 180) {
        alert("You hit the enemy!");
    }
}