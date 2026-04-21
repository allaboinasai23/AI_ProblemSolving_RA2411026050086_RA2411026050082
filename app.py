import streamlit as st
from TicTacToe.tictactoe import get_best_move, check_winner
from Sudoku.sudoku_solver import solve_sudoku

# -----------------------------
# SESSION STATE FOR TIC TAC TOE
# -----------------------------
if "board" not in st.session_state:
    st.session_state.board = [" "] * 9

st.title("AI Problem Solving Project")

menu = st.sidebar.selectbox(
    "Choose Problem",
    ["Tic-Tac-Toe AI", "Sudoku Solver"]
)

# -----------------------------
# TIC TAC TOE
# -----------------------------
if menu == "Tic-Tac-Toe AI":
    st.header("Tic-Tac-Toe AI (Minimax vs Alpha-Beta)")

    method = st.selectbox("Choose Algorithm", ["Minimax", "Alpha-Beta"])

    board = st.session_state.board
    cols = st.columns(3)

    for i in range(9):
        if cols[i % 3].button(board[i], key=i):
            if board[i] == " ":
                board[i] = "X"

                move, t, nodes = get_best_move(board, method)

                if move != -1:
                    board[move] = "O"

                st.write(f"Execution Time: {t:.5f} sec")
                st.write(f"Nodes Explored: {nodes}")

    winner = check_winner(board)
    if winner:
        st.success(f"Result: {winner}")

    if st.button("Restart Game"):
        st.session_state.board = [" "] * 9

# -----------------------------
# SUDOKU SOLVER
# -----------------------------
elif menu == "Sudoku Solver":
    st.header("Sudoku Solver (CSP - Backtracking)")

    grid = []

    for i in range(9):
        row = st.text_input(
            f"Row {i+1} (use space-separated values, 0 for empty)",
            "0 0 0 0 0 0 0 0 0"
        )
        grid.append([int(x) for x in row.split()])

    if st.button("Solve Sudoku"):
        if solve_sudoku(grid):
            st.success("Solved Sudoku:")
            for r in grid:
                st.write(r)
        else:
            st.error("No solution exists")