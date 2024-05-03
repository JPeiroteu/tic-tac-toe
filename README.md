# TicTacToe IoT Fusion

Welcome to TicTacToe IoT Fusion, an innovative project that combines IoT technology with the classic game of Tic-Tac-Toe to create an immersive and interactive gaming experience.

## Overview

TicTacToe IoT Fusion offers players a unique gaming experience where they can seamlessly transition between the physical and digital realms. Using handmade pressure pads embedded in the physical game board, players interact with the game, triggering actions that are synchronized with the web application. This synchronization ensures that every move made on the physical board is immediately reflected in the digital interface, providing a cohesive and immersive gameplay experience.

## Features

- **Hybrid Gameplay Experience:** Seamlessly transition between physical and remote gameplay modes, catering to both local and online players.
- **Web-Based Game Management:** Employ a Flask-powered Python web server as the central hub for overseeing game states, rules, and facilitating real-time communication among players.
- **Physical Game Board with ESP32 Control:** Immerse yourself in gameplay with a physical game board enhanced by handmade pressure pads embedded within. These sensors, controlled by an ESP32 microcontroller, bridge the gap between the physical and digital realms, offering players dynamic visual feedback through integrated LED strips. Each cell is illuminated with a blue tint for "X" and green for "O," providing immediate feedback on player moves and game state changes.
- **Simple Web App Interface:** Access a user-friendly web application interface tailored for remote players. This intuitive platform enables online participants to seamlessly engage with the game board and partake in synchronized gameplay alongside physical players.
- **Scalable Architecture:** Crafted with scalability and adaptability in mind, the project's architecture sets the stage for future enhancements and expansions. This ensures ongoing enrichment of the gaming experience for all players.

## Getting Started

To get started with TicTacToe IoT Fusion, follow these steps:

1. **Clone the Repository:** Clone the repository to your local machine using the following command:
git clone https://github.com/JPeiroteu/tictactoe-iot-fusion.git

2. **Install Dependencies:** Navigate to the project directory and install the necessary dependencies by running:
pip install flask

3. **Start the Web Server:** Run the following command to start the Python-based web server:
python app.py

4. **Access the Web Interface:** Open your web browser and navigate to `http://localhost:5000` to access the web application interface. From there, you can play the game remotely or interact with the physical game board.

5. **Access the Online Web Interface:** Open your web browser and navigate to [http://94.63.14.247:5000/](http://94.63.14.247:5000/) to access the online web application interface. From there, you can play the game remotely or interact with the physical game board. Only when my server is available.

## Code Structure

The repository is organized as follows:

- **app.py:** The main Python script responsible for running the Flask web server and managing game logic.
- **board.py:** Contains the logic for creating and managing the game board, including checking for winners and resetting the board.
- **cell.py:** Defines the Cell class representing individual cells on the game board.
- **game.py:** Implements the Game class for managing gameplay interactions and player moves.
- **index.html:** The HTML template for the web application interface, providing a user-friendly way to play the game remotely.
- **script.js:** JavaScript code for handling client-side interactions and updating the game board interface dynamically.
- **static/style.css:** CSS stylesheet for styling the web interface.

## Arduino Integration

The Arduino code seamlessly integrates with the Python backend, enabling real-time communication and control of the LED strip. Leveraging the FastLED library, the Arduino code effectively manages the LED strip's illumination, synchronizing it with the game state updates received from the server.

For detailed implementation and code, please refer to the [TTTArduino repository](https://github.com/JPeiroteu/TTTArduino).
## Contributing

Contributions to TicTacToe IoT Fusion are welcome! Whether it's bug fixes, feature enhancements, or new ideas, feel free to open an issue or submit a pull request to contribute to the project's development