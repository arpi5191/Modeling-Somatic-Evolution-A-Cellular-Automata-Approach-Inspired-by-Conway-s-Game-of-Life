import numpy as np
import random
from base_functions import in_field

def play_game_of_life_with_mutation(initial_board, num_gens=10000, mutation_rate=0.0, mutation_magnitude=0.0):
    board = np.array(initial_board, dtype=int)
    rows, cols = board.shape

    lonely = np.full((rows, cols), 2)
    born = np.full((rows, cols), 3)
    crowded = np.full((rows, cols), 3)

    steady_state_counter = 0

    for gen in range(num_gens):
        new_board = np.zeros((rows, cols), dtype=int)
        new_lonely = lonely.copy()
        new_born = born.copy()
        new_crowded = crowded.copy()

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                neighborhood = board[i-1:i+2, j-1:j+2]
                num_neighbors = np.sum(neighborhood) - board[i, j]

                cell_lonely = lonely[i, j]
                cell_born = born[i, j]
                cell_crowded = crowded[i, j]

                if board[i, j] == 1:
                    if num_neighbors < cell_lonely or num_neighbors > cell_crowded:
                        new_board[i, j] = 0
                    else:
                        new_board[i, j] = 1
                else:
                    if num_neighbors == cell_born:
                        new_board[i, j] = 1
                        live_neighbors = [(x, y) for x in range(i-1, i+2) for y in range(j-1, j+2)
                                          if (x != i or y != j) and board[x, y] == 1]
                        if live_neighbors:
                            parent_x, parent_y = random.choice(live_neighbors)
                            new_lonely[i, j] = lonely[parent_x, parent_y]
                            new_born[i, j] = born[parent_x, parent_y]
                            new_crowded[i, j] = crowded[parent_x, parent_y]

                        if random.random() < mutation_rate:
                            threshold = random.choice(['lonely', 'born', 'crowded'])
                            delta = int(round(np.random.normal(0, mutation_magnitude)))
                            if threshold == 'lonely':
                                new_lonely[i, j] = np.clip(new_lonely[i, j] + delta, 0, 8)
                            elif threshold == 'born':
                                new_born[i, j] = np.clip(new_born[i, j] + delta, 0, 8)
                            elif threshold == 'crowded':
                                new_crowded[i, j] = np.clip(new_crowded[i, j] + delta, 0, 8)

        if np.array_equal(board, new_board):
            steady_state_counter += 1
        else:
            steady_state_counter = 0

        if steady_state_counter >= 10:
            return gen + 1  # steady-state generation

        board = new_board
        lonely = new_lonely
        born = new_born
        crowded = new_crowded

    return num_gens  # Did not reach steady-state
