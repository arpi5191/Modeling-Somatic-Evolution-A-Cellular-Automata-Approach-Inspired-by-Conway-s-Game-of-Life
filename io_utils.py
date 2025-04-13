import csv

def read_board_from_file(filename):
    """
    Reads a Game of Life board from a CSV file and converts it into a 2D list of booleans.
    
    Parameters:
    filename (str): The path to the CSV file containing the board data.
    
    Returns:
    list: A 2D list representing the board, where True indicates a live cell and False indicates a dead cell.
    """
    board = []  # Initialize an empty list to store the board rows
    
    # Open the CSV file for reading
    with open(filename, 'r') as f:
        # Iterate over each line in the file
        for line in f:
            # Split the line by commas, strip whitespace, and filter out empty values
            row = [val.strip() for val in line.strip().split(',') if val.strip()]
            
            # Convert each value in the row to a boolean (True for '1', False for '0')
            board.append([val == "1" for val in row])
    
    return board  # Return the 2D list representing the board
