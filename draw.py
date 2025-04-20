# draw.py

# Import package
from PIL import Image, ImageDraw

def draw_game_board(board, cell_width, bg_color='black', cell_color='limegreen', shape='ellipse'):
    """
    Draw a board for the Game of Life.

    Parameters:
    board (list): A list of values that the board will be based on.
    cell_width (int): The width of each cell.
    bg_color (str): The background color of the board.
    cell_color (str): The color of the live cells.
    shape (str): The shape of the live cells (ellipse, rectangle, or circle_inset).

    Returns:
    Image: An image of the drawn board.
    """

    # Count the number of rows and columns in the board
    num_rows = len(board)  
    num_cols = len(board[0])  

    # Draw a new image of the board with the background color
    img = Image.new('RGB', (num_cols * cell_width, num_rows * cell_width), bg_color)
    draw = ImageDraw.Draw(img) 

    # Iterate through the rows in the board
    for i in range(num_rows):
        # Iterate through the columns in the board
        for j in range(num_cols):
            # If the cell is alive, find the coordinates based on the cell width
            if board[i][j]:  
                x0 = j * cell_width
                y0 = i * cell_width
                x1 = x0 + cell_width
                y1 = y0 + cell_width

                # Check if the shape is an ellipse and draw it if so
                if shape == 'ellipse':
                    draw.ellipse([x0, y0, x1, y1], fill=cell_color)
                # Check if the shape is a rectangle and draw it if so
                elif shape == 'rectangle':
                    draw.rectangle([x0, y0, x1, y1], fill=cell_color)
                # Check if the shape is a circle inset and draw it if so
                elif shape == 'circle_inset':
                    padding = int(0.1 * cell_width)
                    draw.ellipse([x0 + padding, y0 + padding, x1 - padding, y1 - padding], fill=cell_color)

    # Return the image
    return img

def draw_game_boards(boards, cell_width, bg_color='black', cell_color='limegreen', shape='ellipse'):
    """
    Draw the boards for the Game of Life.

    Parameters:
    boards (list): A list of the boards that will be used in the Game of Life.
    cell_width (int): The width of each cell.
    bg_color (str): The background color of the board.
    cell_color (str): The color of the live cells in the board.
    shape (str): The shape of the live cells (ellipse, rectangle, or circle_inset).
    
    Returns:
    list: A list of images.
    """
    # Draw each board in the list of boards
    return [draw_game_board(board, cell_width, bg_color, cell_color, shape) for board in boards]

def save_gif(images, filename, duration=300):
    """
    Save a list of images as an animated GIF.

    Parameters:
    images (list): A list of images to be saved in the GIF.
    filename (str): The filename to save the GIF as.
    duration (int): The duration of time each frame is displayed (in milliseconds).

    Returns:
    None
    """
    # Save the images to the file with the specified duration.
    images[0].save(filename, save_all=True, append_images=images[1:], optimize=False, duration=duration, loop=0)