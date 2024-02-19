document.addEventListener("DOMContentLoaded", function() {
    const playButton = document.getElementById("playButton");
    const pageTitle = document.getElementById("pageTitle");
    const turnMessage = document.getElementById("turnMessage");
    const board = document.getElementById("board");
    //const updateInterval = setInterval(updateBoard, 5000);

    pageTitle.style.display = "block";
    turnMessage.style.display = "none";
    board.style.display = "none";
    resetButton.style.display = "none";

    let currentPlayer = "X";

    playButton.addEventListener("click", function() {
        playButton.style.display = "none";
        turnMessage.style.display = "block";
        board.style.display = "grid";
        resetButton.style.display = "block";  

        updateTurnMessage();

        updateBoard();
    });

    document.querySelectorAll(".cell").forEach(function(cell) {
        cell.addEventListener("click", function() {
            const [x, y] = cell.id.split('-').slice(1);

            const xhr = new XMLHttpRequest();
            xhr.open("POST", "/cell/mark", true);
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded; charset=UTF-8");
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    const data = JSON.parse(xhr.responseText);
                    cell.innerText = data.result;
                    updateBoard();
                    currentPlayer = currentPlayer === "X" ? "O" : "X";
                    updateTurnMessage();
                    
                    checkWinner();
                }
            };
            xhr.send(`x=${x}&y=${y}&mark=${currentPlayer}`);
        });
    });

    function updateBoard() {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "/board", true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                const data = JSON.parse(xhr.responseText);
                data.grid.forEach(cell => {
                    const cellId = `cell-${cell.x}-${cell.y}`;
                    const cellElement = document.getElementById(cellId);
                    cellElement.innerText = cell.marker;
                    cellElement.setAttribute("data-marker", cell.marker);
                });
            }
        };
        xhr.send();
    }

    function updateTurnMessage() {
        turnMessage.innerText = `${currentPlayer} player's turn`;
    }

    function checkWinner() {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "/check_winner", true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                const winnerData = JSON.parse(xhr.responseText);
                if (winnerData.winner) {
                    turnMessage.innerText = `${winnerData.winner} wins!`;
                } else if (winnerData.draw) {
                    turnMessage.innerText = "It's a draw!";
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

    function resetBoard() {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "/reset_board", true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                updateBoard();
            }
        };
        xhr.send();
    }

});
