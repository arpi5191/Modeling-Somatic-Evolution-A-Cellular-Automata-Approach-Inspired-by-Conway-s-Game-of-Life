# Modeling Somatic Evolution: A Cellular Automata Approach Inspired by Conway's Game of Life
## Introduction
The purpose of our project was to examine how heritable mutations in cell populations can trigger tumor-like growth, thereby enriching our understanding of cancer biology and potential therapeutic strategies. To achieve this, we modified the traditional rules of Conway’s Game of Life (GOL) to add lonely, birth, and crowded thresholds, and to incorporate radiation therapy. Cellular automata (CA) are rule-based models known for their ability to simulate complex systems using simple interactions. Conway’s Game of Life (GOL), a two-dimensional simulation, is a widely known CA in which each cell is either live or dead and updates its life, death, and rebirth based on its living neighbors. Despite these simple rules, GOL is known for producing complex and unpredictable behavior. These outcomes are useful for studying biological processes ranging from the reproduction of unicellular organisms (Sarukhanian et al., 2023) to the disorganized growth of multicellular tissues, such as tumors (Hillen et al., 2013).

## Methodology
Our GOL board is designed to randomize a grid of live and dead cells based on initial constraints and output a .csv file of the final board, following the rules of the game over multiple generations. These .csv files are then used to visually create the boards and GIFs of the board’s progression before reaching a steady state. We then ran and created visualizations of GOL without any modifications to confirm that the results made sense.

Our model runs with the following rules:
   1) A live cell with fewer than two live neighbors dies out (the “loneliness” rule).
   2) A live cell with two or three live neighbors survives to the next generation (not subject to mutation).
   3) A live cell with more than three live neighbors dies out (the “crowded” rule).
   4) A dead cell with exactly three live neighbors becomes a live cell (the “born” rule).

## Usage Guide
1. Run "GoL.ipynb" in a code editor like Jupyter Notebook to perform the following tasks:
   - Initialize and save the board to a file.
   - Run the simulation to generate the boards, draw the image and GIF, and graph the live cell count over the generations, following the original Game of Life rules.
   - Run the simulation to generate graphs of the modified Game of Life rules showing the steady states, live-cell counts, population sizes, average loneliness threshold, average born threshold, and average crowded threshold.
   - Run the simulation to generate graphs of the born-again thresholds, including the effects of radiation.

## Helper Files and Folders
1. io.utils.py: Reads the initial board from the file.
2. base_functions.py: Has all the standard functions from GOL which will be run from GoL.ipynb.
3. mutation_functions.py versions: Contains modified GOL versions that will be run from GoL.ipynb.
4. draw.py: Draws the final board for the simulation.
5. boards folder: Stores initial board.
6. output: Contains all the output graphs and images.
7. output_gifs: Contains all the output gifs.
