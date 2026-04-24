# 🧠 AI Problem Solving

**Repository:** `AI_ProblemSolving_RA2411026050086_RA2411026050082`

---

### 🌐 Live Interactive Website
> **URL:** `https://ai-problemsolving-ra2411026050086-ra2411026050082.onrender.com`

---

## 📁 Folder Structure

```
AI_ProblemSolving_RA2411026050086_RA2411026050082/
├── app.py                     # Flask backend — all game logic & API routes
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── templates/
    ├── home.html              # Unified launcher with game switcher tabs
    ├── index.html             # Tic-Tac-Toe interactive GUI
    └── sudoku.html            # Sudoku interactive GUI
```

---

## 🎮 Problem 1: Tic-Tac-Toe AI

### Problem Description
Build an AI opponent for a web-based Tic-Tac-Toe game where the computer always makes the **best possible move**. The user interacts via an interactive GUI.

### Algorithms Used

| Algorithm | Description |
|-----------|-------------|
| **Minimax** | Explores the entire game tree recursively to find the optimal move. Evaluates all possible future states. |
| **Alpha-Beta Pruning** | An optimized version of Minimax that prunes branches that cannot influence the final decision, significantly reducing computation. |

### Algorithm Comparison

| Metric | Minimax | Alpha-Beta Pruning |
|--------|---------|-------------------|
| Nodes Explored (first move) | ~55,000 | ~2,300 |
| Execution Time | ~243 ms | ~8.8 ms |
| Pruning Savings | — | **~95.8% fewer nodes** |

### Features
- **Single Player** — Play against an unbeatable AI
- **Multiplayer** — Two players on the same board
- **Real-time Comparison** — See nodes explored, execution time, and pruning savings per move
- **Visual Bar Chart** — Nodes explored history across moves
- **Scoreboard** — Track wins, losses, and draws

### Sample Output
- User plays as **X**, AI plays as **O**
- After each AI move, the stats panel shows:
  - Minimax: 55504 nodes, 243.240 ms
  - Alpha-Beta: 2315 nodes, 8.821 ms
  - Pruning Savings: **95.8%** fewer nodes

---

## 🧩 Problem 2: Sudoku Solver

### Problem Description
A 9×9 Sudoku puzzle where the user fills in empty cells through an interactive GUI. The system evaluates the solution ("You won" / "Try again") and can auto-solve using AI.

### Algorithm Used

| Algorithm | Description |
|-----------|-------------|
| **CSP (Constraint Satisfaction Problem)** | Models Sudoku as a CSP where each empty cell is a variable with domain {1–9}. Uses **Backtracking** with **MRV (Minimum Remaining Values)** heuristic for efficient solving. |

### Constraints Enforced
- ✅ Each **row** contains digits 1–9 without repetition
- ✅ Each **column** contains digits 1–9 without repetition
- ✅ Each **3×3 subgrid** contains digits 1–9 without repetition

### Features
- **Interactive Grid** — Click cells and use numpad or keyboard to fill numbers
- **Keyboard Support** — Arrow keys for navigation, number keys for input
- **Check Solution** — Validates user's answer with "🎉 You won!" or "❌ Try again"
- **Error Highlighting** — Cells violating constraints are highlighted in red
- **Auto Solve (CSP)** — AI solves the puzzle instantly (~1-15 ms) and displays the solution
- **Multiple Puzzles** — 4 different puzzles with "New Puzzle" button
- **Cell Highlighting** — Selected cell highlights its row, column, and 3×3 box

### Sample Output
- Pre-filled puzzle displayed with given numbers in purple
- User fills empty cells (shown in pink)
- Click "Check Solution" → **"🎉 You won! The solution is correct!"**
- Click "Auto Solve (CSP)" → Grid fills with solution in green, shows **"CSP Solve Time: 2.15 ms"**

---

## 🚀 Execution Steps

### Prerequisites
- Python 3.8+ installed
- pip (Python package manager)

### Installation & Run

```bash
# 1. Clone the repository
git clone https://github.com/allaboinasai23/AI_ProblemSolving_RA2411026050086_RA2411026050082.git
cd AI_ProblemSolving_RA2411026050086_RA2411026050082

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python app.py

# 4. Open in browser
# Visit: http://127.0.0.1:5000
```

### Usage
1. Open `http://127.0.0.1:5000` in your browser
2. Use the **tab switcher** at the top to switch between games
3. **Tic-Tac-Toe:** Click cells to play, view AI comparison stats on the right
4. **Sudoku:** Click a cell → click a number on the numpad → Check or Auto-Solve

---

## 🛠️ Technologies Used
- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **AI Algorithms:** Minimax, Alpha-Beta Pruning, CSP with Backtracking + MRV
- **Deployment:** Render

---

## 👥 Contributors
- RA2411026050086
- RA2411026050082
