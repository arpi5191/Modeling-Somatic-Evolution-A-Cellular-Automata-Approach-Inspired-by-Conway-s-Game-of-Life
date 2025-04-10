import csv

def read_board_from_file(filename):
    board = []
    with open(filename, 'r') as f:
        for line in f:
            row = [val.strip() for val in line.strip().split(',') if val.strip()]
            board.append([val == "1" for val in row])
    return board
