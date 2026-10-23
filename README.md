# Tic-Tac-Toe

A two-player command-line tic-tac-toe game written in Python.

Players take turns placing **X** and **O** on a 3×3 board. The first player to get three in a row (horizontally, vertically, or diagonally) wins. If the board fills with no winner, the game is a tie.

## Requirements

- Python 3

## How to run

From this folder:

```bash
python tictactoe.py
```

On some systems you may need `python3` instead of `python`.

## How to play

1. Player **X** goes first.
2. On each turn, enter a **row** and **column** as two numbers from 1 to 3, separated by a space.
   - Example: `2 3` places a mark in row 2, column 3.
3. Invalid moves (wrong format, out of range, or a taken cell) are rejected and you try again.
4. Press `Ctrl+C` to quit mid-game.

## Files

- `tictactoe.py` — game logic and the play loop
