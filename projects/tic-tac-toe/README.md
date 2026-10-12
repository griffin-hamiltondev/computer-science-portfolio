# Tic-Tac-Toe

A Python desktop application built with Tkinter that lets users play Tic-Tac-Toe against another player or a computer opponent with three difficulty levels.

## Features

* **Player vs Player:** Play locally with two human players.
* **Player vs Computer:** Play against a computer opponent.
* **Three AI difficulty levels:**

  * **Easy:** Selects a random available square.
  * **Medium:** Attempts to block the player's winning moves.
  * **Hard:** Attempts to win when possible and blocks the player when necessary.
* **Win detection:** Detects when a player completes a winning line.
* **Tie detection:** Detects when the board is full without a winner.
* **Winning line highlighting:** Highlights the winning combination.
* **Reset game:** Start a new game without restarting the application.

## Technologies Used

* Python 3
* Tkinter (graphical user interface)
* Random module (computer move selection)

## How to Run

1. Install Python 3.
2. Ensure Tkinter is available in your Python installation.
3. Open a terminal in the project directory.
4. Run the application:

   ```bash
   python3 tic_tac_toe.py
   ```

## How to Play

### Player vs Player

1. Select the **Multiplayer** option.
2. Players take turns placing X and O on the board.
3. The first player to complete a line of three symbols horizontally, vertically, or diagonally wins.

### Player vs Computer

1. Select the **Computer** option.
2. Choose an AI difficulty level.
3. Play against the computer by selecting an available square.

## Development Process

The project was developed incrementally:

1. Implemented the core Player vs Player game.
2. Added an Easy computer opponent.
3. Added Medium difficulty with blocking behaviour.
4. Implemented the reset functionality.
5. Added Hard difficulty with winning and blocking logic.
6. Tested features as they were implemented.

## What I Learned

* Building graphical user interfaces with Tkinter.
* Managing game state and player turns.
* Working with nested lists to represent a game board.
* Implementing win and tie detection.
* Developing computer opponent logic with different difficulty levels.
* Building and testing a project incrementally.

## Possible Future Improvements

* Score tracking across multiple rounds.
* Allowing the computer to make the first move.
* Implementing a minimax-based AI.
* Supporting custom board sizes.
* Improving the visual styling.
* Adding sound effects.
