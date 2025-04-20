import copy

def initialize_board(num_rows, num_cols):
    """
    Initialize a board with the specified number of rows and columns.

    Parameters:
    num_rows (int): Number of rows in the board.
    num_cols (int): Number of columns in the board.

    Returns:
    list: A 2D list containing False in all cells, indicating that each cell is dead.
    """
    return [[False for _ in range(num_cols)] for _ in range(num_rows)]

def update_cell(board, r, c):
    """
    Update the cell based on Conway's Game of Life rules.

    Parameters:
    board (list): A 2D list representing the current state of the board.
    r (int): Row index of the cell that should be updated.
    c (int): Column index of the cell that should be updated.

    Returns:
    bool: The updated state of the cell (True for live, False for dead).
    """
    # Count the number of live neighbors the cell has
    num_neighbors = count_live_neighbors(board, r, c)

    # Update the cell based on the Game of Life rules
    if board[r][c]:
        return num_neighbors == 2 or num_neighbors == 3
    else:
        return num_neighbors == 3

def update_board(board):
    """
    Update the board based on Conway's Game of Life rules.

    Parameters:
    board (list): A list of values that the board currently contains.
    
    Returns:
    list: A list of values that the new board will contain.
    """
    # Count the number of rows and columns in the board
    num_rows = len(board)
    num_cols = len(board[0])

    # Initialize the board with the number of rows and columns
    new_board = initialize_board(num_rows, num_cols)

    # Iterate through the rows
    for r in range(num_rows):
        # Iterate through the columns
        for c in range(num_cols):
            # Update the cell in the board based on Conway's Game of Life rules
            new_board[r][c] = update_cell(board, r, c)

    # Return the new board
    return new_board

def play_game_of_life(initial_board, num_gens):
    """
    Play the Game of Life over the specified number of generations unless steady state is reached sooner.

    Parameters:
    initial_board (list): The initial board (2D list of cell states).
    num_gens (int): The number of generations that the Game of Life should be run for unless steady state is reached sooner.

    Returns:
    boards (tuple): A list of boards generated over the generations from the game.
    """

    # Add the initial board to the boards list
    boards = [initial_board]

    # Iterate through the generations
    for _ in range(num_gens):
        # Update the board and add it to the list
        boards.append(update_board(boards[-1]))

    # Return the boards generated from the game
    return boards

def count_live_neighbors(board, r, c):
    """
    Count the number of live neighbors that the cell has. 

    Parameters:
    board (list): The current board (2D list of cell states).
    r (int): Row index of the cell whose neighbors are being counted.
    c (int): Column index of the cell whose neighbors are being counted.

    Returns:
    int: The number of live neighbors that the cell has.
    """

    # Initialize the count
    count = 0

    # Iterate through the cell's neighboring rows
    for i in range(r - 1, r + 2):
        # Iterate through the cell's neighboring columns
        for j in range(c - 1, c + 2):
            # Check if the indices don't match the cell whose neighbors are being counted and that the cell is within the board
            if (i != r or j != c) and in_field(board, i, j):
                # If the cell is alive, increment the count
                if board[i][j]:
                    count += 1

    # Return the number of live neighbors
    return count

def in_field(board, i, j):
    """
    Check if the input coordinates (i, j) are within the board.

    Parameters:
    board (list): The current board (2D list of cell states).
    i (int): Row index of the cell to check.
    j (int): Column index of the cell to check.

    Returns:
    bool: True if (i, j) is within the board, False otherwise.
    """
    return 0 <= i < len(board) and 0 <= j < len(board[0])