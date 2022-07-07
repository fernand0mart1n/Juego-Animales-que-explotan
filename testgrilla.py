try:
    import tkinter as tk
    import tkinter.ttk as ttk
except ImportError:
    import Tkinter as tk
    import ttk 

import random

# --- constants --- (UPPER_CASE names)

ROWS = 8 
COLUMNS = 8 
CELL_WIDTH = 50 
CELL_HEIGHT = 50
BANDITS_NUMBER = 5

# --- functions ---

def create_grid():

    data = {}

    for col in range(COLUMNS):
        for row in range(ROWS):
            x1 = col * CELL_WIDTH 
            y1 = row * CELL_HEIGHT
            x2 = x1 + CELL_WIDTH 
            y2 = y1 + CELL_HEIGHT
            data[row, col] = game_grid.create_rectangle(x1, y1, x2, y2,
                                                       fill="green", tags="rect")

    return data   

def create_bandits(image):

    data = {}

    for i in range(BANDITS_NUMBER):

        while True:
            row = random.randint(0, ROWS-1)
            col = random.randint(0, COLUMNS-1)
            if (row,col) not in data:
                break

        x1 = col * CELL_WIDTH + 22
        y1 = row * CELL_HEIGHT - 22
        x2 = x1 + CELL_WIDTH
        y2 = y1 + CELL_HEIGHT

        data[row, col] = game_grid.create_image(x1, y2, image=image)

    return data

# --- main ---

# - init -

window = tk.Tk() 

game_frame = tk.Frame(window)
game_frame.pack()

game_grid = tk.Canvas(game_frame, width=450, height=450, borderwidth=0,
                      highlightthickness=0)
game_grid.pack()
game_grid.itemconfig("rect", fill="green")

# - data -

rects = create_grid()

# create global variable
bandit_image = tk.PhotoImage(file="Bandit.png")

# send image to function - so you don't need word "global"
bandits = create_bandits(bandit_image)

# - start -

window.mainloop()