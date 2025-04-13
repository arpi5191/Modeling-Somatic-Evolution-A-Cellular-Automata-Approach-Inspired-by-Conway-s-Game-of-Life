import copy
import numpy as np

def initialize_board(num_rows, num_cols):
    """
    Initialize a 2D board with all cells set to False (dead).

    Parameters:
    num_rows (int): Number of rows in the board.
    num_cols (int): Number of columns in the board.

    Returns:
    list: A 2D list (board) with all cells initialized to False (dead).
    """
    # Initialize the board with 'False' (dead) cells
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
    # Count the number of live neighbors of the current cell
    num_neighbors = count_live_neighbors(board, r, c)

    # Apply the Game of Life rules to update the cell
    if board[r][c]:  # If the cell is currently live
        return num_neighbors == 2 or num_neighbors == 3  # The cell survives if it has 2 or 3 neighbors
    else:  # If the cell is currently dead
        return num_neighbors == 3  # The cell becomes live if it has exactly 3 neighbors

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

    # Initialize a new board to hold the next generation
    new_board = initialize_board(num_rows, num_cols)

    # Update each cell in the new board based on its neighbors
    for r in range(1, num_rows - 1):  # Skip the edges to avoid boundary issues
        for c in range(1, num_cols - 1):
            new_board[r][c] = update_cell(board, r, c)  # Update the cell's state based on the Game of Life rules

    return new_board  # Return the new board representing the next generation

def play_game_of_life(initial_board, num_gens):
    """
    Run the Game of Life simulation for a specified number of generations.

    Parameters:
    initial_board (list): The initial board configuration (2D list of cell states).
    num_gens (int): The number of generations to run the simulation.

    Returns:
    tuple: A tuple containing the list of boards (one for each generation) and the list of population counts for each generation.
    """
    # Convert initial board to numpy array for consistency
    initial_board = np.array(initial_board)

    # Initialize a list to store the boards for each generation
    boards = [initial_board]

    # Initialize the population list, counting the live cells (True represents live cells)
    populations = [np.count_nonzero(initial_board)]  # Count live cells directly

    # Simulate the Game of Life for the specified number of generations
    for _ in range(num_gens):

        # Generate the next board based on the current board
        boards.append(update_board(boards[-1]))

        # Count the live cells in the new board and append to the population list
        populations.append(np.count_nonzero(boards[-1]))

        # Stop if the population reaches a steady state (no changes in board)
        if np.array_equal(boards[-2], boards[-1]):
            break  # Exit the loop if the board has reached a steady state

    return boards, populations  # Return the list of boards and the population counts

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
    count = 0  # Initialize the neighbor count to 0

    # Loop through the 3x3 neighborhood around the cell (including diagonals)
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            # Exclude the current cell and ensure it's within the field of the board
            if (i != r or j != c) and in_field(board, i, j):
                if board[i][j]:  # If the neighbor is live
                    count += 1  # Increment the count of live neighbors

    return count  # Return the total count of live neighbors

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
    return 0 < i < (len(board) - 1) and 0 < j < (len(board[0]) - 1)  # Ensure the indices are within the board's valid range
