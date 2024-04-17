
document.addEventListener("DOMContentLoaded", function() {
    const playButton = document.getElementById("playButton");
    const pageTitle = document.getElementById("pageTitle");
    const turnMessage = document.getElementById("turnMessage");
    const board = document.getElementById("board");

    pageTitle.style.display = "block";
    turnMessage.style.display = "none";
    board.style.display = "none";
    resetButton.style.display = "none";
    setInterval(updateBoard, 1000);
    setInterval(function() {
        getCurrentPlayer(updateTurnMessage);
    }, 1000);
    setInterval(checkWinner, 1000);


    let currentPlayer;

    playButton.addEventListener("click", function() {
        playButton.style.display = "none";
        turnMessage.style.display = "block";
        board.style.display = "grid";
        resetButton.style.display = "block";

        getCurrentPlayer(updateTurnMessage);
        updateBoard();
        checkWinner();
    });

    board.addEventListener("click", function(event) {
        if (event.target.classList.contains("cell")) {
            const [x, y] = event.target.id.split('-').slice(1);
            makeMove(x, y, currentPlayer, event);
        }
    });

    function getCurrentPlayer(callback) {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "/player/current", true);
        xhr.onload = function() {
            if (xhr.status === 200) {
                const data = JSON.parse(xhr.responseText);
                currentPlayer = data.currentPlayer;
                callback();
            }
        };
        xhr.send();
    }
    
    function makeMove(x, y, player, event) {
        const xhr = new XMLHttpRequest();
        xhr.open("POST", "/cell/mark", true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded; charset=UTF-8");
        xhr.onload = function() {
            if (xhr.status === 200) {
                const data = JSON.parse(xhr.responseText);
                event.target.textContent = data.result; 
                getCurrentPlayer(updateTurnMessage);
                updateBoard();
                checkWinner();
            }
        };
        xhr.send(`x=${x}&y=${y}&mark=${player}`);
    }    

    function updateBoard() {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "/board", true);
        xhr.onload = function() {
            if (xhr.status === 200) {
                const data = JSON.parse(xhr.responseText);
                data.grid.forEach(function(cell) {
                    const cellElement = document.getElementById(`cell-${cell.x}-${cell.y}`);
                    cellElement.textContent = cell.marker;
                    cellElement.dataset.marker = cell.marker;
                });
            }
        };
        xhr.send();
    }

    function updateTurnMessage() {
        turnMessage.textContent = currentPlayer + "'s turn";
    }

    // Function to check for a winner
    function checkWinner() {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "/check_winner", true);
        xhr.onload = function() {
            if (xhr.status === 200) {
                const winnerData = JSON.parse(xhr.responseText);
                if (winnerData.win_cell.marker) {
                    const winnerMarker = winnerData.win_cell.marker;
                    turnMessage.textContent = winnerMarker + " wins!";
                } else if (winnerData.draw) {
                    turnMessage.textContent = "It's a draw!";
                }
            }
        };
        xhr.send();
    }
    

    resetButton.addEventListener("click", function() {
        resetButton.style.display = "none";
        turnMessage.innerText = "";
        resetBoard();
    });

    // Function to reset the board
    function resetBoard() {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "/reset_board", true);
        xhr.onload = function() {
            if (xhr.status === 200) {
                updateBoard();
            }
        };
        xhr.send();
        location.reload();
    }
});