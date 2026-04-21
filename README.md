# AI Problem Solving Project

This project contains two classic AI problem-solving implementations built with a Streamlit interface. 

## Features

1. **Tic-Tac-Toe AI:**
   - Play Tic-Tac-Toe against an AI.
   - Choose between **Minimax** and **Alpha-Beta Pruning** algorithms to see the difference in performance.
   - The interface displays the execution time and number of nodes explored for each move.

2. **Sudoku Solver:**
   - Solves Sudoku puzzles using **Constraint Satisfaction Problem (CSP) / Backtracking**.
   - Input a custom 9x9 grid to find its solution.

## Project Structure

- `app.py`: The main Streamlit application script containing the UI.
- `TicTacToe/tictactoe.py`: The backend logic for the Tic-Tac-Toe game and the Minimax/Alpha-Beta algorithms.
- `Sudoku/sudoku_solver.py`: The backend logic for solving Sudoku using backtracking.
- `requirements.txt`: Python package dependencies.

## Installation and Setup

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/allaboinasai23/AI_ProblemSolving_RA2411026050086_RA2411026050082.git
   cd AI_ProblemSolving_RA2411026050086_RA2411026050082
   ```

2. **Install the requirements**:
   Ensure you have Python installed. Then, run the following command to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```
   This will open the application in your default web browser where you can switch between the two AI problems in the sidebar.

## Usage

* **Tic-Tac-Toe**: Select the problem from the sidebar, choose your desired algorithm, and start playing by clicking on the empty squares. The AI plays as 'O'.
* **Sudoku**: Enter the rows of your Sudoku puzzle in the provided input fields (use `0` for empty cells, separated by spaces), and click 'Solve Sudoku'.