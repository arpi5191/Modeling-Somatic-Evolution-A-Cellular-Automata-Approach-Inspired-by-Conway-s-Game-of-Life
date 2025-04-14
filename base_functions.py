import copy

def initialize_board(num_rows, num_cols):
    """
    Initialize a 2D board with all cells set to False (dead).

    Parameters:
    num_rows (int): Number of rows in the board.
    num_cols (int): Number of columns in the board.

    Returns:
    list: A 2D list (board) with all cells initialized to False (dead).
    """
    return [[False for _ in range(num_cols)] for _ in range(num_rows)]

def update_cell(board, r, c):
    """
    Update the state of a single cell based on the Conway's Game of Life rules.

    Parameters:
    board (list): The current board (2D list of cell states).
    r (int): Row index of the cell to be updated.
    c (int): Column index of the cell to be updated.

    Returns:
    bool: The updated state of the cell (True for live, False for dead).
    """
    num_neighbors = count_live_neighbors(board, r, c)
    if board[r][c]:
        return num_neighbors == 2 or num_neighbors == 3
    else:
        return num_neighbors == 3

def update_board(board):
    """
    Update the entire board for the next generation based on the Conway's Game of Life rules.

    Parameters:
    board (list): The current board (2D list of cell states).

    Returns:
    list: A new board (2D list) representing the next generation.
    """
    num_rows = len(board)
    num_cols = len(board[0])
    new_board = initialize_board(num_rows, num_cols)
    for r in range(num_rows):
        for c in range(num_cols):
            new_board[r][c] = update_cell(board, r, c)
    return new_board

def play_game_of_life(initial_board, num_gens):
    """
    Run the Game of Life simulation for a specified number of generations.

    Parameters:
    initial_board (list): The initial board configuration (2D list of cell states).
    num_gens (int): The number of generations to run the simulation.

    Returns:
    tuple: A tuple containing the list of boards (one for each generation) and the list of population counts for each generation.
    """
    boards = [initial_board]
    for _ in range(num_gens):
        boards.append(update_board(boards[-1]))
    return boards

def count_live_neighbors(board, r, c):
    """
    Count the number of live neighbors around a specific cell.

    Parameters:
    board (list): The current board (2D list of cell states).
    r (int): Row index of the cell whose neighbors are being counted.
    c (int): Column index of the cell whose neighbors are being counted.

    Returns:
    int: The number of live neighbors around the specified cell.
    """
    count = 0
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if (i != r or j != c) and in_field(board, i, j):
                if board[i][j]:
                    count += 1
    return count

def in_field(board, i, j):
    """
    Check if the given coordinates (i, j) are within the valid bounds of the board.

    Parameters:
    board (list): The current board (2D list of cell states).
    i (int): The row index to check.
    j (int): The column index to check.

    Returns:
    bool: True if (i, j) is within the bounds of the board, False otherwise.
    """
    return 0 <= i < len(board) and 0 <= j < len(board[0])
