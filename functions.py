import copy

def initialize_board(num_rows, num_cols):
    return [[False for _ in range(num_cols)] for _ in range(num_rows)]

def update_cell(board, r, c):
    num_neighbors = count_live_neighbors(board, r, c)
    if board[r][c]:
        return num_neighbors == 2 or num_neighbors == 3
    else:
        return num_neighbors == 3

def update_board(board):
    num_rows = len(board)
    num_cols = len(board[0])
    new_board = initialize_board(num_rows, num_cols)
    for r in range(num_rows):
        for c in range(num_cols):
            new_board[r][c] = update_cell(board, r, c)
    return new_board

def play_game_of_life(initial_board, num_gens):
    boards = [initial_board]
    for _ in range(num_gens):
        boards.append(update_board(boards[-1]))
    return boards

def count_live_neighbors(board, r, c):
    count = 0
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if (i != r or j != c) and in_field(board, i, j):
                if board[i][j]:
                    count += 1
    return count

def in_field(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])
