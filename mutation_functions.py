# Import packages
import numpy as np
import random
from base_functions import in_field

def play_game_of_life_with_mutation(initial_board, num_gens=10000, mutation_rate=0.0, mutation_magnitude=0.0):
    """
    Simulates the Game of Life applying thresholds with mutation over the specified number of generations.

    Parameters:
    initial_board (list): The initial board (2D list of cell states).
    num_gens (int): The number of generations the Game of Life is played.
    mutation_rate (float): The probability that a mutation occurs during cell birth.
    mutation_magnitude (float): The magnitude of the mutation applied to thresholds.

    Returns:
    int: Number of generations until steady state is reached, or the maximum number of generations if steady state is not reached.
    """

    # Initialize the main board
    board = np.array(initial_board, dtype=int)

    # Initialize the lonely, born, and crowded boards based on the number of rows and columns
    rows, cols = board.shape
    lonely = np.full((rows, cols), 2)
    born = np.full((rows, cols), 3)
    crowded = np.full((rows, cols), 3)

    # Iterate through each generation
    for gen in range(num_gens):

        # Initialize the new board based on the number of rows and columns
        new_board = np.zeros((rows, cols), dtype=int)

        # Copy the lonely, born, and crowded boards
        new_lonely = lonely.copy()
        new_born = born.copy()
        new_crowded = crowded.copy()

        # Iterate through each inner row in the board
        for i in range(1, rows - 1):
            # Iterate through each inner column in the board
            for j in range(1, cols - 1):

                # Obtain the neighborhood of the cell and find the number of live neighbors the cell has
                neighborhood = board[i-1:i+2, j-1:j+2]
                num_neighbors = np.sum(neighborhood) - board[i, j]

                # Round the values in the lonely, born, and crowded boards at position (i, j)
                cell_lonely = int(round(lonely[i, j]))  
                cell_born = int(round(born[i, j]))      
                cell_crowded = int(round(crowded[i, j]))

                # Check if the cell was alive in the last generation
                if board[i, j] == 1:
                    # Check if the cell dies in the current generation based on the conditions
                    if num_neighbors < cell_lonely or num_neighbors > cell_crowded:
                        # Reset the threshold values if the cell dies
                        new_board[i, j] = 0
                        new_lonely[i, j] = 2
                        new_born[i, j] = 3
                        new_crowded[i, j] = 3
                    else:
                        # Otherwise, keep the cell alive
                        new_board[i, j] = 1
                # Otherwise, check if the cell is dead
                else:
                    # Check if the cell becomes alive in the current generation
                    if num_neighbors == cell_born:
                        # Set the board value to 1
                        new_board[i, j] = 1
                        # Select a random live neighbor as the parent
                        live_neighbors = [(x, y) for x in range(i-1, i+2) for y in range(j-1, j+2)
                                          if (x != i or y != j) and board[x, y] == 1]
                        # Check if there are live neighbors
                        if live_neighbors:
                            # Randomly choose one of the live neighbors
                            parent_x, parent_y = random.choice(live_neighbors)
                            # The thresholds at position (i, j) inherit from the randomly selected live neighbor
                            new_lonely[i, j] = lonely[parent_x, parent_y]
                            new_born[i, j] = born[parent_x, parent_y]
                            new_crowded[i, j] = crowded[parent_x, parent_y]
                            
                            # Apply mutation with specified probability
                            if random.random() < mutation_rate:
                                # Randomly select a threshold to mutate
                                threshold = random.choice(['lonely', 'born', 'crowded'])
                                # Multiply the mutation magnitude with a value from a normal distribution
                                delta = mutation_magnitude * np.random.normal(0, 1)

                                # Update the threshold value with delta and clip it within bounds of 0 and 8
                                if threshold == 'lonely':
                                    new_lonely[i, j] = np.clip(new_lonely[i, j] + delta, 0, 8)
                                elif threshold == 'born':
                                    new_born[i, j] = np.clip(new_born[i, j] + delta, 0, 8)
                                elif threshold == 'crowded':
                                    new_crowded[i, j] = np.clip(new_crowded[i, j] + delta, 0, 8)
        
        # Check if the board from the last generation is the same as this generation
        if np.array_equal(board, new_board):
            # Return the generation if the steady state is reached
            return gen + 1  

        # Update the boards
        board = new_board
        lonely = new_lonely
        born = new_born
        crowded = new_crowded
    
    # Return number of generations if steady state wasn't reached
    return num_gens

def simulate_population_with_mutation(initial_board, num_gens=10000, mutation_rate=0.0, mutation_magnitude=0.0):
    """
    Simulates the Game of Life applying thresholds with mutation over the specified number of generations.

    Parameters:
    initial_board (list): The initial board (2D list of cell states).
    num_gens (int): The number of generations the Game of Life is played.
    mutation_rate (float): The probability that a mutation occurs during cell birth.
    mutation_magnitude (float): The magnitude of the mutation applied to thresholds.

    Returns:
    int: Population of the final board.
    """

    # Initialize the main board
    board = np.array(initial_board, dtype=int)

    # Initialize the lonely, born, and crowded boards based on the number of rows and columns
    rows, cols = board.shape
    lonely = np.full((rows, cols), 2)
    born = np.full((rows, cols), 3)
    crowded = np.full((rows, cols), 3)

    # Iterate through each generation
    for gen in range(num_gens):

        # Initialize the new board based on the number of rows and columns
        new_board = np.zeros((rows, cols), dtype=int)

        # Copy the lonely, born, and crowded boards
        new_lonely = lonely.copy()
        new_born = born.copy()
        new_crowded = crowded.copy()

        # Iterate through each inner row in the board
        for i in range(1, rows - 1):
            # Iterate through each inner column in the board
            for j in range(1, cols - 1):

                # Obtain the neighborhood of the cell and find the number of live neighbors the cell has
                neighborhood = board[i-1:i+2, j-1:j+2]
                num_neighbors = np.sum(neighborhood) - board[i, j]

                # Round the values in the lonely, born, and crowded boards at position (i, j)
                cell_lonely = int(round(lonely[i, j]))  
                cell_born = int(round(born[i, j]))      
                cell_crowded = int(round(crowded[i, j]))

                # Check if the cell was alive in the last generation
                if board[i, j] == 1:
                    # Check if the cell dies in the current generation based on the conditions
                    if num_neighbors < cell_lonely or num_neighbors > cell_crowded:
                        # Reset the threshold values if the cell dies
                        new_board[i, j] = 0
                        new_lonely[i, j] = 2
                        new_born[i, j] = 3
                        new_crowded[i, j] = 3
                    else:
                        # Otherwise, keep the cell alive
                        new_board[i, j] = 1
                # Otherwise, check if the cell is dead
                else:
                    # Check if the cell becomes alive in the current generation
                    if num_neighbors == cell_born:
                        # Set the board value to 1
                        new_board[i, j] = 1
                        # Select a random live neighbor as the parent
                        live_neighbors = [(x, y) for x in range(i-1, i+2) for y in range(j-1, j+2)
                                          if (x != i or y != j) and board[x, y] == 1]
                        # Check if there are live neighbors
                        if live_neighbors:
                            # Randomly choose one of the live neighbors
                            parent_x, parent_y = random.choice(live_neighbors)
                            # The thresholds at position (i, j) inherit from the randomly selected live neighbor
                            new_lonely[i, j] = lonely[parent_x, parent_y]
                            new_born[i, j] = born[parent_x, parent_y]
                            new_crowded[i, j] = crowded[parent_x, parent_y]
                            
                            # Apply mutation with specified probability
                            if random.random() < mutation_rate:
                                # Randomly select a threshold to mutate
                                threshold = random.choice(['lonely', 'born', 'crowded'])
                                # Multiply the mutation magnitude with a value from a normal distribution
                                delta = mutation_magnitude * np.random.normal(0, 1)

                                # Update the threshold value with delta and clip it within bounds of 0 and 8
                                if threshold == 'lonely':
                                    new_lonely[i, j] = np.clip(new_lonely[i, j] + delta, 0, 8)
                                elif threshold == 'born':
                                    new_born[i, j] = np.clip(new_born[i, j] + delta, 0, 8)
                                elif threshold == 'crowded':
                                    new_crowded[i, j] = np.clip(new_crowded[i, j] + delta, 0, 8)
        
        # Check if the board from the last generation is the same as this generation
        if np.array_equal(board, new_board):
            # Return the board's population if steady state was reached
            return np.sum(new_board)  

        # Update the boards
        board = new_board
        lonely = new_lonely
        born = new_born
        crowded = new_crowded
    
    # Return the board's population if steady state wasn't reached
    return np.sum(board)