import numpy as np
import random
from base_functions import in_field

def play_game_of_life_with_radiation(initial_board, num_gens=10000, mutation_rate=0.4, mutation_magnitude=1.5, rad_strength=0, gen_gap=4):
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
    damage = np.full((rows, cols), rad_strength)
    lonely = np.full((rows, cols), 2.0)
    born = np.full((rows, cols), 2.0)
    crowded = np.full((rows, cols), 3.0)

    steady_state_count = 0
    """
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if board[i][j] == 0: 
                print("set to -1")
                born[i][j] = -1 
    """


    # Initialize a list to store the population of live cells over the generations
    population = []

    # Iterate through each generation
    for gen in range(num_gens): 
        print(gen)


        # Initialize the new board based on the number of rows and columns
        new_board = np.zeros((rows, cols), dtype=int)

        # Copy the lonely, born, and crowded boards
        new_lonely = lonely.copy()
        new_born = born.copy()
        new_crowded = crowded.copy()
        new_damage = damage.copy()

        # Iterate through each inner row in the board (skip borders)
        for i in range(1, rows - 1):
            # Iterate through each inner column in the board
            for j in range(1, cols - 1):
                
                raddeath = False
                # Obtain the neighborhood of the cell and find the number of live neighbors the cell has
                neighborhood = board[i-1:i+2, j-1:j+2]
                num_neighbors = np.sum(neighborhood) - board[i, j]

                # Round the values in the lonely, born, and crowded boards at position (i, j)

                if board[i, j] == 0:
                    live_neighbors = [(x, y) for x in range(i-1, i+2) for y in range(j-1, j+2)
                                          if (x != i or y != j) and board[x, y] == 1]
                    if live_neighbors:
                        parent_x, parent_y = random.choice(live_neighbors) 
                        cell_born = int(round(born[parent_x, parent_y]))
                    # Check if the cell becomes alive in the current generation
                        if num_neighbors <= cell_born:
                            # Set the board value to 1
                            new_board[i, j] = 1
                            # Check if there are live neighbors
                            if live_neighbors:
                                # The thresholds at position (i, j) inherit from the randomly selected live neighbor
                                new_lonely[i, j] = lonely[parent_x, parent_y]
                                new_born[i, j] = cell_born
                                new_crowded[i, j] = crowded[parent_x, parent_y]
                                new_damage[i, j] = damage[parent_x, parent_y]
                            
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
                # Check if the cell is alive
                cell_lonely = int(round(new_lonely[i, j]))  
                cell_born = int(round(new_born[i, j]))      
                cell_crowded = int(round(new_crowded[i, j]))
                if new_board[i, j] == 1 or board[i,j] == 1:
                    if gen % gen_gap == 0: 
                        new_damage[i,j] = new_damage[i,j] + rad_strength

                    improvement = (new_born[i, j]) / 20

                    new_damage[i,j] = max(0,new_damage[i,j]-improvement)
                    if ((gen + round(gen_gap/2) % gen_gap)) == 0: 
                        if new_damage[i,j] > 0: 
                            raddeath = True
                    # Check if the cell dies in the current generation based on the conditions
                    if num_neighbors < cell_lonely or num_neighbors > cell_crowded or raddeath:
                        # Reset the threshold values if the cell dies
                        new_board[i, j] = 0
                        new_lonely[i, j] = 2.0
                        new_crowded[i, j] = 3.0
                        new_damage[i,j] = -1
                # Otherwise, check if the cell is dead

        # Store the population of the live cells
        boards.append(new_board)
        population.append(np.sum(new_board))

        # Check if the new board is the same for 10 consecutive generations

        # Update the boards
        board = new_board
        lonely = new_lonely
        born = new_born
        crowded = new_crowded
        damage = new_damage
    
    # Return the number of generations, population and board if steady state wasn't reached, and a list of the mutation threshold changes
    return [num_gens, population, board, born, np.sum(board), np.mean(lonely), np.mean(born), np.mean(crowded), boards]