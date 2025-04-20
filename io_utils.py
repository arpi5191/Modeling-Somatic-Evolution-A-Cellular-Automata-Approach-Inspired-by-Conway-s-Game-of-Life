import csv

def read_board_from_file(filename):
    """
    Reads the board from the input filename.
    
    Parameters:
    filename (str): The path to the file where the board is saved.
    
    Returns:
    list: A 2D array that contains a 1 if the cell is alive and a 0 if it is dead.
    """

    # Create an empty list to hold the values in the board
    board = [] 
    

    # Open the file in read mode
    with open(filename, 'r') as f:
        # Iterate through each line in the file
        for line in f:
            # Split the row of the board into values using a comma as a delimiter
            row = [val.strip() for val in line.strip().split(',') if val.strip()]
            # Add a 1 for every value in the row
            board.append([val == "1" for val in row])

    # Return the board
    return board  
