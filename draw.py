# draw.py

from PIL import Image, ImageDraw

def draw_game_board(board, cell_width, bg_color='black', cell_color='limegreen', shape='ellipse'):
    """
    Draw a single Game of Life board as an image.

    Parameters:
    board (list): The board to be drawn (2D list of cell states).
    cell_width (int): The width and height of each cell in pixels.
    bg_color (str): The background color of the board.
    cell_color (str): The color of the live cells.
    shape (str): The shape of the live cells (ellipse, rectangle, or circle_inset).

    Returns:
    Image: An image representing the drawn Game of Life board.
    """
    num_rows = len(board)  # Get the number of rows in the board
    num_cols = len(board[0])  # Get the number of columns in the board

    # Create a new image with the specified background color and size based on the board's dimensions
    img = Image.new('RGB', (num_cols * cell_width, num_rows * cell_width), bg_color)
    draw = ImageDraw.Draw(img)  # Create a drawing context for the image

    # Loop through each cell in the board
    for i in range(num_rows):
        for j in range(num_cols):
            if board[i][j]:  # Only draw live cells (cells that are True)
                # Calculate the coordinates of the cell's top-left and bottom-right corners
                x0 = j * cell_width
                y0 = i * cell_width
                x1 = x0 + cell_width
                y1 = y0 + cell_width

                # Draw the cell based on the specified shape
                if shape == 'ellipse':
                    draw.ellipse([x0, y0, x1, y1], fill=cell_color)  # Draw an ellipse for the cell
                elif shape == 'rectangle':
                    draw.rectangle([x0, y0, x1, y1], fill=cell_color)  # Draw a rectangle for the cell
                elif shape == 'circle_inset':
                    # Draw a circle inset within the cell, with padding around it
                    padding = int(0.1 * cell_width)
                    draw.ellipse([x0 + padding, y0 + padding, x1 - padding, y1 - padding], fill=cell_color)

    return img  # Return the image representing the drawn board

def draw_game_boards(boards, cell_width, bg_color='black', cell_color='limegreen', shape='ellipse'):
    """
    Draw multiple Game of Life boards as images.

    Parameters:
    boards (list): A list of boards to be drawn (each is a 2D list of cell states).
    cell_width (int): The width and height of each cell in pixels.
    bg_color (str): The background color of the boards.
    cell_color (str): The color of the live cells.
    shape (str): The shape of the live cells (ellipse, rectangle, or circle_inset).
    
    Returns:
    list: A list of images representing the drawn Game of Life boards.
    """
    # Draw each board and return the list of images
    return [draw_game_board(board, cell_width, bg_color, cell_color, shape) for board in boards]

def save_gif(images, filename, duration=300):
    """
    Save a list of images as an animated GIF.

    Parameters:
    images (list): A list of images to be included in the GIF.
    filename (str): The filename to save the GIF as.
    duration (int): The duration (in milliseconds) for each frame of the GIF.

    Returns:
    None
    """
    # Save the images as an animated GIF with the specified duration and filename
    images[0].save(filename, save_all=True, append_images=images[1:], optimize=False, duration=duration, loop=0)
