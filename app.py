"""
Tic-Tac-Toe AI — Minimax vs Alpha-Beta Pruning
A Flask web application that lets a user play Tic-Tac-Toe against an AI opponent.
The AI computes the best move using both Minimax and Alpha-Beta Pruning,
then compares execution time and nodes explored.
"""

import time
import copy
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# ──────────────────────────────────────────────
# Game Logic Helpers
# ──────────────────────────────────────────────

def check_winner(board):
    """Return 'X', 'O', or None."""
    lines = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    for line in lines:
        if line[0] == line[1] == line[2] and line[0] is not None:
            return line[0]
    return None


def is_board_full(board):
    return all(board[r][c] is not None for r in range(3) for c in range(3))


def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] is None]


# ──────────────────────────────────────────────
# Minimax Algorithm (plain)
# ──────────────────────────────────────────────

def minimax(board, is_maximizing, stats):
    """
    Pure Minimax without pruning.
    AI plays 'O' (maximizing), Human plays 'X' (minimizing).
    Returns the evaluation score.
    """
    stats["nodes"] += 1

    winner = check_winner(board)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best = -float("inf")
        for r, c in get_available_moves(board):
            board[r][c] = "O"
            score = minimax(board, False, stats)
            board[r][c] = None
            best = max(best, score)
        return best
    else:
        best = float("inf")
        for r, c in get_available_moves(board):
            board[r][c] = "X"
            score = minimax(board, True, stats)
            board[r][c] = None
            best = min(best, score)
        return best


def best_move_minimax(board):
    """Find the best move for 'O' using plain Minimax."""
    stats = {"nodes": 0}
    start = time.perf_counter()

    best_score = -float("inf")
    move = None
    for r, c in get_available_moves(board):
        board[r][c] = "O"
        score = minimax(board, False, stats)
        board[r][c] = None
        if score > best_score:
            best_score = score
            move = (r, c)

    elapsed = time.perf_counter() - start
    return move, stats["nodes"], elapsed


# ──────────────────────────────────────────────
# Alpha-Beta Pruning
# ──────────────────────────────────────────────

def alphabeta(board, is_maximizing, alpha, beta, stats):
    """
    Minimax with Alpha-Beta Pruning.
    Returns the evaluation score.
    """
    stats["nodes"] += 1

    winner = check_winner(board)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best = -float("inf")
        for r, c in get_available_moves(board):
            board[r][c] = "O"
            score = alphabeta(board, False, alpha, beta, stats)
            board[r][c] = None
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # β cut-off
        return best
    else:
        best = float("inf")
        for r, c in get_available_moves(board):
            board[r][c] = "X"
            score = alphabeta(board, True, alpha, beta, stats)
            board[r][c] = None
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:
                break  # α cut-off
        return best


def best_move_alphabeta(board):
    """Find the best move for 'O' using Alpha-Beta Pruning."""
    stats = {"nodes": 0}
    start = time.perf_counter()

    best_score = -float("inf")
    move = None
    alpha = -float("inf")
    beta = float("inf")

    for r, c in get_available_moves(board):
        board[r][c] = "O"
        score = alphabeta(board, False, alpha, beta, stats)
        board[r][c] = None
        if score > best_score:
            best_score = score
            move = (r, c)
        alpha = max(alpha, best_score)

    elapsed = time.perf_counter() - start
    return move, stats["nodes"], elapsed


# ──────────────────────────────────────────────
# Flask Routes
# ──────────────────────────────────────────────

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/tictactoe")
def tictactoe():
    return render_template("index.html")


@app.route("/api/move", methods=["POST"])
def api_move():
    """
    Receive the current board, compute AI move with BOTH algorithms,
    and return the chosen move along with comparison metrics.
    """
    data = request.get_json()
    board = data.get("board")  # 3×3 list, None / 'X' / 'O'

    # Run both algorithms on a deep copy so they don't interfere
    board_copy1 = copy.deepcopy(board)
    board_copy2 = copy.deepcopy(board)

    move_mm, nodes_mm, time_mm = best_move_minimax(board_copy1)
    move_ab, nodes_ab, time_ab = best_move_alphabeta(board_copy2)

    # Both algorithms should return the same optimal move
    # We'll use the Alpha-Beta result (faster) as the actual move
    chosen = move_ab if move_ab else move_mm

    if chosen is None:
        return jsonify({"error": "No moves available"}), 400

    return jsonify({
        "move": {"row": chosen[0], "col": chosen[1]},
        "minimax": {
            "nodes": nodes_mm,
            "time_ms": round(time_mm * 1000, 4),
        },
        "alphabeta": {
            "nodes": nodes_ab,
            "time_ms": round(time_ab * 1000, 4),
        },
    })


# ──────────────────────────────────────────────
# Sudoku — CSP Solver
# ──────────────────────────────────────────────

import random

# Sample puzzles (0 = empty)
SUDOKU_PUZZLES = [
    [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9],
    ],
    [
        [0,0,0,2,6,0,7,0,1],
        [6,8,0,0,7,0,0,9,0],
        [1,9,0,0,0,4,5,0,0],
        [8,2,0,1,0,0,0,4,0],
        [0,0,4,6,0,2,9,0,0],
        [0,5,0,0,0,3,0,2,8],
        [0,0,9,3,0,0,0,7,4],
        [0,4,0,0,5,0,0,3,6],
        [7,0,3,0,1,8,0,0,0],
    ],
    [
        [0,0,0,6,0,0,4,0,0],
        [7,0,0,0,0,3,6,0,0],
        [0,0,0,0,9,1,0,8,0],
        [0,0,0,0,0,0,0,0,0],
        [0,5,0,1,8,0,0,0,3],
        [0,0,0,3,0,6,0,4,5],
        [0,4,0,2,0,0,0,6,0],
        [9,0,3,0,0,0,0,0,0],
        [0,2,0,0,0,0,1,0,0],
    ],
    [
        [2,0,0,3,0,0,0,0,0],
        [8,0,4,0,6,2,0,0,3],
        [0,1,3,8,0,0,2,0,0],
        [0,0,0,0,2,0,3,9,0],
        [5,0,7,0,0,0,6,2,1],
        [0,3,2,0,0,6,0,0,0],
        [0,2,0,0,0,9,1,4,0],
        [6,0,1,2,5,0,8,0,9],
        [0,0,0,0,0,1,0,0,2],
    ],
]


def get_candidates(grid, row, col):
    """Return set of valid digits for cell (row, col) using CSP constraints."""
    if grid[row][col] != 0:
        return set()
    used = set()
    # Row constraint
    used.update(grid[row])
    # Column constraint
    for r in range(9):
        used.add(grid[r][col])
    # 3×3 subgrid constraint
    br, bc = 3 * (row // 3), 3 * (col // 3)
    for r in range(br, br + 3):
        for c in range(bc, bc + 3):
            used.add(grid[r][c])
    used.discard(0)
    return set(range(1, 10)) - used


def solve_sudoku_csp(grid):
    """
    Solve Sudoku using CSP with backtracking + MRV (Minimum Remaining Values).
    Returns True if solved (modifies grid in-place).
    """
    # Find the empty cell with fewest candidates (MRV heuristic)
    best_cell = None
    best_candidates = None
    min_count = 10

    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                cands = get_candidates(grid, r, c)
                if len(cands) == 0:
                    return False  # Dead end
                if len(cands) < min_count:
                    min_count = len(cands)
                    best_cell = (r, c)
                    best_candidates = cands

    if best_cell is None:
        return True  # All cells filled — solved!

    r, c = best_cell
    for val in best_candidates:
        grid[r][c] = val
        if solve_sudoku_csp(grid):
            return True
        grid[r][c] = 0  # Backtrack

    return False


def validate_sudoku(grid):
    """Check if a completed 9×9 grid is a valid Sudoku solution."""
    for i in range(9):
        row = [grid[i][j] for j in range(9)]
        col = [grid[j][i] for j in range(9)]
        if sorted(row) != list(range(1, 10)):
            return False
        if sorted(col) != list(range(1, 10)):
            return False
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            block = []
            for r in range(br, br + 3):
                for c in range(bc, bc + 3):
                    block.append(grid[r][c])
            if sorted(block) != list(range(1, 10)):
                return False
    return True


# ──────────────────────────────────────────────
# Sudoku Flask Routes
# ──────────────────────────────────────────────

@app.route("/sudoku")
def sudoku_page():
    return render_template("sudoku.html")


@app.route("/api/sudoku/puzzle", methods=["GET"])
def api_sudoku_puzzle():
    """Return a random Sudoku puzzle."""
    puzzle = copy.deepcopy(random.choice(SUDOKU_PUZZLES))
    return jsonify({"puzzle": puzzle})


@app.route("/api/sudoku/validate", methods=["POST"])
def api_sudoku_validate():
    """Validate the user's submitted Sudoku grid."""
    data = request.get_json()
    grid = data.get("grid")

    # Check for incomplete
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0 or grid[r][c] is None:
                return jsonify({"valid": False, "message": "Puzzle is not complete. Fill all cells!"})

    is_valid = validate_sudoku(grid)
    if is_valid:
        return jsonify({"valid": True, "message": "🎉 You won! The solution is correct!"})
    else:
        return jsonify({"valid": False, "message": "❌ Try again — some constraints are violated."})


@app.route("/api/sudoku/solve", methods=["POST"])
def api_sudoku_solve():
    """Solve the puzzle using CSP and return the solution."""
    data = request.get_json()
    grid = copy.deepcopy(data.get("grid"))

    start = time.perf_counter()
    solved = solve_sudoku_csp(grid)
    elapsed = time.perf_counter() - start

    if solved:
        return jsonify({"solved": True, "grid": grid, "time_ms": round(elapsed * 1000, 2)})
    else:
        return jsonify({"solved": False, "message": "No solution exists for this puzzle."})


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
