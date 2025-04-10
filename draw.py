# draw.py

from PIL import Image, ImageDraw

def draw_game_board(board, cell_width, bg_color='black', cell_color='limegreen', shape='ellipse'):
    num_rows = len(board)
    num_cols = len(board[0])
    
    img = Image.new('RGB', (num_cols * cell_width, num_rows * cell_width), bg_color)
    draw = ImageDraw.Draw(img)

    for i in range(num_rows):
        for j in range(num_cols):
            if board[i][j]:
                x0 = j * cell_width
                y0 = i * cell_width
                x1 = x0 + cell_width
                y1 = y0 + cell_width
                if shape == 'ellipse':
                    draw.ellipse([x0, y0, x1, y1], fill=cell_color)
                elif shape == 'rectangle':
                    draw.rectangle([x0, y0, x1, y1], fill=cell_color)
                elif shape == 'circle_inset':
                    padding = int(0.1 * cell_width)
                    draw.ellipse([x0 + padding, y0 + padding, x1 - padding, y1 - padding], fill=cell_color)
    return img

def draw_game_boards(boards, cell_width, bg_color='black', cell_color='limegreen', shape='ellipse'):
    return [draw_game_board(board, cell_width, bg_color, cell_color, shape) for board in boards]

def save_gif(images, filename, duration=300):
    images[0].save(filename, save_all=True, append_images=images[1:], optimize=False, duration=duration, loop=0)
