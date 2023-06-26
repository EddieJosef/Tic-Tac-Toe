# Tic Tac Toe

This repository contains a simple Tic Tac Toe game implemented in Python scripting. The game allows two players to take turns placing their marks ('X' or 'O') on a 3x3 game board until one of them wins or the game ends in a draw.

## Game Rules

- The game board is represented by a list of strings with nine elements, initialized as follows:
    ```python
    game_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    ```

- The board is displayed after each move using the `show_board()` function.

- Players take turns entering the location where they want to place their mark. The board locations are numbered from 1 to 9 as shown below:
    ```
    ---+-----+---
    1  |  2  |  3
    ---+-----+---
    4  |  5  |  6
    ---+-----+---
    7  |  8  |  9
    ```

- To make a move, players need to enter the location number when prompted.

- The game checks for a win condition after each move using the `check_win()` function. A player wins if they have three of their marks in a row, column, or diagonal.

- The game continues until one of the players wins or the game ends in a draw.

## Usage

To play the Tic Tac Toe game, run the `game()` function. The game will prompt you to choose your character by entering 1 for 'X' or 2 for 'O'. Each player will take turns making moves until a win condition is met or the game ends.

```python
game()
```

Enjoy playing Tic Tac Toe!

