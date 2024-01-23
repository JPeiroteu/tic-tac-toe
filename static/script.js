document.addEventListener('DOMContentLoaded', function () {
    const playButton = document.getElementById('playButton');
    const pageTitle = document.getElementById('pageTitle');
    const turnMessage = document.getElementById('turnMessage');
    const board = document.getElementById('board');

    let currentPlayer = '🐔';  //🐭
    let gameBoard = [];

    playButton.addEventListener('click', function () {
        for (let i = 0; i < 9; i++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            cell.dataset.x = i % 3;
            cell.dataset.y = Math.floor(i / 3);
            board.appendChild(cell);
            gameBoard.push(cell);
        }

        playButton.style.display = 'none';
        pageTitle.innerText = 'Tic-Tac-Toe';
        turnMessage.innerText = `${currentPlayer} Player's Turn`;
    });


    
});



