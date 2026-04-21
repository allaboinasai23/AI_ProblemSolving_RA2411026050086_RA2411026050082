import time

minimax_nodes = 0
alphabeta_nodes = 0

def check_winner(b):
    win_states = [(0,1,2),(3,4,5),(6,7,8),
                  (0,3,6),(1,4,7),(2,5,8),
                  (0,4,8),(2,4,6)]
    for x,y,z in win_states:
        if b[x] == b[y] == b[z] and b[x] != " ":
            return b[x]
    if " " not in b:
        return "Draw"
    return None

def minimax(b, is_max):
    global minimax_nodes
    minimax_nodes += 1

    result = check_winner(b)
    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "Draw":
        return 0

    if is_max:
        best = -1000
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = max(best, minimax(b, False))
                b[i] = " "
        return best
    else:
        best = 1000
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = min(best, minimax(b, True))
                b[i] = " "
        return best

def alphabeta(b, is_max, alpha, beta):
    global alphabeta_nodes
    alphabeta_nodes += 1

    result = check_winner(b)
    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "Draw":
        return 0

    if is_max:
        best = -1000
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                val = alphabeta(b, False, alpha, beta)
                b[i] = " "
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = 1000
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                val = alphabeta(b, True, alpha, beta)
                b[i] = " "
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

def get_best_move(b, method):
    global minimax_nodes, alphabeta_nodes
    minimax_nodes = 0
    alphabeta_nodes = 0

    best_val = -1000
    move = -1

    start = time.time()

    for i in range(9):
        if b[i] == " ":
            b[i] = "O"

            if method == "Minimax":
                val = minimax(b, False)
            else:
                val = alphabeta(b, False, -1000, 1000)

            b[i] = " "

            if val > best_val:
                best_val = val
                move = i

    end = time.time()

    nodes = minimax_nodes if method == "Minimax" else alphabeta_nodes

    return move, end - start, nodes