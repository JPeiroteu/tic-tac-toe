
document.addEventListener("DOMContentLoaded", function() {
    const playButton = document.getElementById("playButton");
    const joinButton = document.getElementById("joinButton");
    const resetButton = document.getElementById("resetButton");
    const pageTitle = document.getElementById("pageTitle");
    const turnMessage = document.getElementById("turnMessage");
    const board = document.getElementById("board");
    const gameIdInput = document.getElementById("gameIdInput");

    pageTitle.style.display = "block";
    turnMessage.style.display = "none";
    board.style.display = "none";
    resetButton.style.display = "none";

    let currentPlayer;
    let currentGameId = null;

    playButton.addEventListener("click", async function() {
        const response = await fetch("/new_game", { method: "POST" });
        const data = await response.json();
        currentGameId = data.game_id;
        gameIdInput.value = currentGameId;
        initializeGame();
    });

    joinButton.addEventListener("click", function() {
        const gameId = parseInt(gameIdInput.value, 10);
        if (!isNaN(gameId)) {
            currentGameId = gameId;
            initializeGame();
        } else {
            alert("Invalid Game ID");
        }
    });

    resetButton.addEventListener("click", async function() {
        if (currentGameId !== null) {
            await fetch(`/game/${currentGameId}/reset_board`, { method: "POST" });
            updateBoard();
        }
    });

    board.addEventListener("click", function(event) {
        if (event.target.classList.contains("cell") && currentGameId !== null) {
            const [x_coord, y_coord] = event.target.id.split('-').slice(1).map(Number);
            makeMove(x_coord, y_coord, currentPlayer, event);
        }
    });

    function initializeGame() {
        playButton.style.display = "none";
        joinButton.style.display = "none";
        turnMessage.style.display = "block";
        board.style.display = "grid";
        resetButton.style.display = "block";
        
        updateBoard();
        getCurrentPlayer(updateTurnMessage);
        setInterval(updateBoard, 1000);
        setInterval(() => getCurrentPlayer(updateTurnMessage), 1000);
        setInterval(checkWinner, 1000);
    }

    function getCurrentPlayer(callback) {
        if (currentGameId !== null) {
            fetch(`/game/${currentGameId}/player/current`)
                .then(response => response.json())
                .then(data => {
                    currentPlayer = data.currentPlayer;
                    callback();
                });
        }
    }

    function makeMove(x_coord, y_coord, player, event) {
        fetch(`/game/${currentGameId}/cell/mark`, {
            method: "POST",
            headers: {
                "Content-type": "application/x-www-form-urlencoded"
            },
            body: `x_coord=${x_coord}&y_coord=${y_coord}&mark=${player}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                event.target.textContent = data.marker;
                getCurrentPlayer(updateTurnMessage);
                updateBoard();
                checkWinner();
            }
        });
    }

    function updateBoard() {
        if (currentGameId !== null) {
            fetch(`/game/${currentGameId}/board`)
                .then(response => response.json())
                .then(data => {
                    data.grid.forEach(cell => {
                        const cellElement = document.getElementById(`cell-${cell.x_coord}-${cell.y_coord}`);
                        cellElement.textContent = cell.marker;
                        cellElement.dataset.marker = cell.marker;
                        if (cell.marker !== " ") {
                            cellElement.classList.add(cell.marker === "X" ? "cell-x" : "cell-o");
                        } else {
                            cellElement.classList.remove("cell-x", "cell-o");
                        }
                    });
                });
        }
    }

    function updateTurnMessage() {
        turnMessage.textContent = currentPlayer ? `${currentPlayer}'s turn` : "";
    }

    function checkWinner() {
        if (currentGameId !== null) {
            fetch(`/game/${currentGameId}/check_winner`)
                .then(response => response.json())
                .then(winnerData => {
                    if (winnerData.win_cell) {
                        const winnerMarker = winnerData.win_cell.marker;
                        turnMessage.textContent = `${winnerMarker} wins!`;
                    } else if (winnerData.winner === "Tie") {
                        turnMessage.textContent = "It's a tie!";
                    }
                });
        }
    }
});
