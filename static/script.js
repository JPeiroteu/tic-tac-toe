document.addEventListener("DOMContentLoaded", function() {
    const boardButton = document.getElementById("boardButton");
    const playButton = document.getElementById("playButton");
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
    let inactivityTimeout; 
    let gameEnded = false; 
    const inactivityDuration = 120000; 

    function resetInactivityTimeout() {
        clearTimeout(inactivityTimeout);
        inactivityTimeout = setTimeout(() => {
            if (currentGameId !== null) {
                location.reload(); // Refresh only if a game is active
            }
        }, inactivityDuration);
    }

    document.addEventListener("click", resetInactivityTimeout);

    resetInactivityTimeout();

    boardButton.addEventListener("click", async function() {
        const gameId = 99;
        currentGameId = gameId; 
        initializeGame(currentGameId);
    });
    
    playButton.addEventListener("click", async function() {
        const gameIdInputValue = gameIdInput.value;
    
        if (gameIdInputValue) {
            const gameId = parseInt(gameIdInputValue, 10);
            if (!isNaN(gameId)) {
                currentGameId = gameId;
                initializeGame(currentGameId);
            } else {
                return alert("Invalid Game ID");
            }
        } else {
            try {
                const response = await fetch("/new_game?timestamp=${Date.now()}", { method: "POST" });
                if (response.ok) {
                    const data = await response.json();
                    currentGameId = data.game_id;
                    gameIdInput.value = currentGameId;
                    initializeGame(currentGameId);
                } else {
                    alert("Failed to create a new game");
                }
            } catch (error) {
                alert("Error connecting to the server");
            }
        }
    });
    
    resetButton.addEventListener("click", async function() {
        if (currentGameId !== null) {
            await fetch(`/game/${currentGameId}/reset_board?timestamp=${Date.now()}`, { method: "POST" });
            updateBoard();
        }
    });

    board.addEventListener("click", function(event) {
        if (event.target.classList.contains("cell") && currentGameId !== null) {
            const [x_coord, y_coord] = event.target.id.split('-').slice(1).map(Number);
            makeMove(x_coord, y_coord, currentPlayer, event);
        }
    });

    async function initializeGame(gameId) {
        try {
            const response = await fetch(`/game/${gameId}/board?timestamp=${Date.now()}`);
            const data = await response.json();
    
            if (data.error) {
                alert(data.error);
                return; 
            }
    
            boardButton.style.display = "none";
            playButton.style.display = "none";
            turnMessage.style.display = "block";
            board.style.display = "grid";
            resetButton.style.display = "block";
    
            updateBoard();
            getCurrentPlayer(updateTurnMessage);
            setInterval(updateBoard, 1000);
            setInterval(() => getCurrentPlayer(updateTurnMessage), 1000);
            setInterval(checkWinner, 1000);
        } catch (error) {
            console.error(error);
        }
    }

    function getCurrentPlayer(callback) {
        if (currentGameId !== null) {
            fetch(`/game/${currentGameId}/player/current?timestamp=${Date.now()}`)
                .then(response => response.json())
                .then(data => {
                    currentPlayer = data.currentPlayer;
                    callback();
                });
        }
    }

    function makeMove(x_coord, y_coord, player, event) {
        fetch(`/game/${currentGameId}/cell/mark?timestamp=${Date.now()}`, {
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
            fetch(`/game/${currentGameId}/board?timestamp=${Date.now()}`)
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
        if (!gameEnded) { 
            turnMessage.textContent = currentPlayer ? `${currentPlayer}'s turn` : "";
        }
    }

    function checkWinner() {
        if (currentGameId !== null) {
            fetch(`/game/${currentGameId}/check_winner?timestamp=${Date.now()}`)
                .then(response => response.json())
                .then(winnerData => {
                    if (winnerData.win_cell) {
                        const winnerMarker = winnerData.win_cell.marker;
                        turnMessage.textContent = `${winnerMarker} wins!`;
                        gameEnded = true; 
                    } else if (winnerData.winner === "Tie") {
                        turnMessage.textContent = "It's a tie!";
                        gameEnded = true; 
                    }
                });
        }
    }
});
