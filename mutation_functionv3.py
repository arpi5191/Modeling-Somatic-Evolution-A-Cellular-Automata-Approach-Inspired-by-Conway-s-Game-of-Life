# Import packages
import numpy as np
import random
from base_functions import in_field
import math

###––––––HELPER FUNCTIONS––––––###

# def at_steadystate(population, generations_to_check):
#     """
#     Determines whether the population has reached a steady state.

#     Parameters:
#     population (list of int): A list of the population of live cells at each generation.
#     generations_to_check (int): How many generations were checked

#     Returns:
#     bool: True if the population has remained constant over the specified number of generations; False otherwise.
#     """

#     # Check that enough generations have occurred to check steady state
#     if len(population) < generations_to_check:
#         return False

#     # Check if the population remains the same for the last 'generations_to_check' generations
#     if len(set(population[-generations_to_check:])) == 1:
#         return True

#     # Steady state has not been reached
#     return False


def play_game_of_life(initial_board, num_gens=10000, mutation_rate=0.0, mutation_magnitude=0.0):
    """
    Simulates the Game of Life with threshold mutations
    Returning the number of generations until steady state is reached, the end population, the lonely, crowded, and born mutationas.

    Parameters:
    initial_board (list): The initial board (2D list of cell states).
    num_gens (int): The number of generations the Game of Life is played.
    mutation_rate (float): The probability that a mutation occurs during cell birth.
    mutation_magnitude (float): The magnitude of the mutation applied to thresholds.

    Returns:
    In a list [
        int: Number of generations until steady state is reached, or the maximum number of generations if steady state is not reached.
        int: The end population after steady state is reached
        float: the final average lonely threshold
        float: the final average born threshold
        float: the final average crowded threshold
    ]
    """
    boards = [] 
    # Initialize the main board
    board = np.array(initial_board, dtype=int)

    # Initialize the lonely, born, and crowded boards based on the number of rows and columns
    rows, cols = board.shape
    lonely = np.full((rows, cols), 2.0)
    born = np.full((rows, cols), 3.0)
    crowded = np.full((rows, cols), 3.0)

    steady_state_count = 0

    # Initialize a list to store the population of live cells over the generations
    population = []

    # Iterate through each generation
    for gen in range(num_gens):
        gen = gen + 1

        # Initialize the new board based on the number of rows and columns
        new_board = np.zeros((rows, cols), dtype=int)

        # Copy the lonely, born, and crowded boards
        new_lonely = lonely.copy()
        new_born = born.copy()
        new_crowded = crowded.copy()

        # Iterate through each inner row in the board (skip borders)
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
                        new_lonely[i, j] = 2.0
                        new_born[i, j] = -1
                        new_crowded[i, j] = 3.0
                    else:
                        # Otherwise, keep the cell alive
                        new_board[i, j] = 1
                # Otherwise, check if the cell is dead
                else:
                    live_neighbors = [(x, y) for x in range(i-1, i+2) for y in range(j-1, j+2)
                                          if (x != i or y != j) and board[x, y] == 1]
                    if live_neighbors:
                        parent_x, parent_y = random.choice(live_neighbors) 
                        cell_born = int(round(born[parent_x, parent_y]))
                    # Check if the cell becomes alive in the current generation
                        if num_neighbors >= cell_born:
                            # Set the board value to 1
                            new_board[i, j] = 1
                            # Check if there are live neighbors
                            if live_neighbors:
                                # The thresholds at position (i, j) inherit from the randomly selected live neighbor
                                new_lonely[i, j] = lonely[parent_x, parent_y]
                                new_born[i, j] = cell_born
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

        # Store the population of the live cells
        boards.append(new_board)
        population.append(np.sum(new_board))

        # Check if the new board is the same for 10 consecutive generations
        if np.array_equal(board, new_board):
            steady_state_count += 1
            if steady_state_count == 10:
                return [gen + 1, population, new_board, new_born, new_crowded, np.sum(new_board), np.mean(new_lonely), np.mean(new_born), np.mean(new_crowded), boards]
        else:
            steady_state_count = 0

        # Update the boards
        board = new_board
        lonely = new_lonely
        born = new_born
        crowded = new_crowded
    
    # Return the number of generations, population and board if steady state wasn't reached, and a list of the mutation threshold changes
    return [num_gens, population, board, born, crowded, np.sum(board), np.mean(lonely), np.mean(born), np.mean(crowded), boards]