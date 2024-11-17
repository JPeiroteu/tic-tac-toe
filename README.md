# TicTacToe IoT Fusion

Welcome to TicTacToe IoT Fusion, an innovative project that combines IoT technology with the classic game of Tic-Tac-Toe to create an immersive and interactive gaming experience.

## Overview

TicTacToe IoT Fusion offers players a unique gaming experience where they can seamlessly transition between the physical and digital realms. Using handmade pressure pads embedded in the physical game board, players interact with the game, triggering actions that are synchronized with the web application. This synchronization ensures that every move made on the physical board is immediately reflected in the digital interface, providing a cohesive and immersive gameplay experience.

### Features

- **Hybrid Gameplay Experience**: Players can switch between physical gameplay on the board and remote gameplay through the web interface.
- **Web-Based Game Management**: The **Flask-powered Python web server** acts as the control hub, managing the game state, rules, and player interactions.
- **Physical Game Board with ESP32 Control**: Handmade pressure pads detect moves on the physical board. LEDs provide real-time visual feedback, with blue lights for "X" and green for "O."
- **Simple Web App Interface**: A user-friendly web interface allows remote players to participate in the game and track the current state of the physical board.
- **Scalable Architecture**: The system is designed to scale and adapt, allowing future upgrades and new features to be added easily.

### Built With

- [**Arduino (C++)**](https://www.arduino.cc/)
- [**Flask (Python)**](https://flask.palletsprojects.com/)
- [**HTML/CSS/JavaScript**](https://developer.mozilla.org/)

## Getting Started

To get started with TicTacToe IoT Fusion, follow these steps:

### Clone the Repository

```bash
git clone https://github.com/JPeiroteu/tictactoe-iot-fusion.git
```

### Install Dependencies

Navigate to the project directory and install the necessary Python dependencies:

```bash
pip install flask flask-limiter
```

### Start the Web Server

Run the following command to start the web server:

```bash
python app.py
```

### Access the Web Interface

Open your browser and navigate to:

- Local: `http://localhost:5000`
- Online (when available): `http://94.63.14.247:5000/`
From there, you can play the game remotely or interact with the physical game board. Only when my server is available.

## Code Structure

The repository is organized as follows:

- **app.py:** The main Python script responsible for running the Flask web server and managing game logic.
- **board.py:** Contains the logic for creating and managing the game board, including checking for winners and resetting the board.
- **cell.py:** Defines the Cell class representing individual cells on the game board.
- **game.py:** Implements the Game class for managing gameplay interactions and player moves.
- **index.html:** The HTML template for the web application interface, providing a user-friendly way to play the game remotely.
- **script.js:** JavaScript code for handling client-side interactions and updating the game board interface dynamically.
- **style.css:** CSS stylesheet for styling the web interface.

## Arduino Integration

The Arduino code seamlessly integrates with the Python backend, enabling real-time communication and control of the LED strip. Leveraging the FastLED library, the Arduino code effectively manages the LED strip's illumination, synchronizing it with the game state updates received from the server.

For detailed implementation and code, please refer to the [TTTArduino repository](https://github.com/JPeiroteu/TTTArduino).

## Contributing

Contributions to TicTacToe IoT Fusion are welcome! Whether it's bug fixes, feature enhancements, or new ideas, feel free to open an issue or submit a pull request to contribute to the project's development
