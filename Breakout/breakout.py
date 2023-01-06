"""
File: Breakout.py
----------------
YOUR DESCRIPTION HERE
"""

import tkinter
import time


# How big is the playing area
CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 800     # Height of drawing canvas in pixels

# Constants for the bricks
N_ROWS = 8              # How many rows of bricks are there?
N_COLS = 10             # How many columns of bricks are there?
SPACING = 5             # How much space is there between each brick?
BRICK_START_X = 5
BRICK_START_Y = 75      # The y coordinate of the top-most brick
BRICK_HEIGHT = 20       # How many pixels high is each brick
BRICK_WIDTH = int((CANVAS_WIDTH - (N_COLS+1) * SPACING ) / N_COLS)

# Constants for the ball and paddle
BALL_SIZE = 30
PADDLE_Y = CANVAS_HEIGHT - 40
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 20



def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Breakout')
    create_bricks(canvas)
    turns = 3
    while turns != 0:
        turn_counter(canvas, turns)
        run_game(canvas)
        turns -= 1
    lose_screen(canvas)
    canvas.mainloop()


def create_bricks(canvas):
    for row in range(N_ROWS):
        for col in range(N_COLS):
            draw_bricks(canvas, row, col)



def draw_bricks(canvas, row, col):
    start_x = BRICK_START_X + (col * (SPACING + BRICK_WIDTH))
    start_y = BRICK_START_Y + (row * (SPACING + BRICK_HEIGHT))
    end_x = start_x + BRICK_WIDTH
    end_y = start_y + BRICK_HEIGHT

    if row == 0 or row == 1:
       canvas.create_rectangle(start_x, start_y, end_x, end_y, fill="firebrick4", outline="firebrick4")

    if row == 2 or row == 3:
        canvas.create_rectangle(start_x, start_y, end_x, end_y, fill="orange", outline="orange")

    if row == 4 or row == 5:
        canvas.create_rectangle(start_x, start_y, end_x, end_y, fill="forest green", outline="forest green")

    if row == 6 or row == 7:
        canvas.create_rectangle(start_x, start_y, end_x, end_y, fill="royal blue", outline="royal blue")





def run_game(canvas):
    ball = canvas.create_oval(275, 375, (275 + BALL_SIZE), (375 + BALL_SIZE), fill="firebrick3")
    dx = 10
    dy = 10
    paddle = canvas.create_rectangle(275, PADDLE_Y, (275 + PADDLE_WIDTH), (PADDLE_Y + PADDLE_HEIGHT), fill="firebrick3")
    top_border = canvas.create_line(0, 65, CANVAS_WIDTH, 65, fill="light grey")


    while True:
        bricks_left = total_bricks(canvas) +1

        canvas.move(ball, dx, dy)

        mouse_x = canvas.winfo_pointerx()
        if 0 <= mouse_x <= 520:
            canvas.moveto(paddle, mouse_x, PADDLE_Y)

        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            dx *= -1

        if hit_bottom_wall(canvas, ball):
            canvas.delete(ball)
            canvas.delete(paddle)
            break

        if bricks_left == 0:
            canvas.delete(ball)
            canvas.delete(paddle)
            canvas.create_text(300, 375, font=("Small Fonts", 33), text="You Won !", fill="light grey")
            canvas.mainloop()


        colliding_list = get_coords_list(canvas, ball)


        if len(colliding_list) > 1:
            dy *= -1
            for object in colliding_list:
                if object != ball and object != paddle and object != top_border:
                    canvas.delete(object)
                    bricks_left -= 1


        canvas.update()
        time.sleep(1/30)


def total_bricks(canvas):
    list = canvas.find_overlapping(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT)
    return (len(list) - 5)




def hit_left_wall(canvas, ball):
    x_coordinate = get_left_x(canvas, ball)
    return x_coordinate <= 0

def hit_right_wall(canvas, ball):
    x_coordinate = get_left_x(canvas, ball) + BALL_SIZE
    return x_coordinate >= CANVAS_WIDTH

def hit_bottom_wall(canvas, ball):
    y_coordinate = get_top_y(canvas, ball) + BALL_SIZE
    return y_coordinate >= CANVAS_HEIGHT




def get_coords_list(canvas, ball):
    ball_coords = canvas.coords(ball)
    x_1 = ball_coords[0]
    y_1 = ball_coords[1]
    x_2 = ball_coords[2]
    y_2 = ball_coords[3]
    return canvas.find_overlapping(x_1, y_1, x_2, y_2)



def get_top_y(canvas, object):
    return canvas.coords(object)[1]

def get_left_x(canvas, object):
    return canvas.coords(object)[0]


def turn_counter(canvas, turns):
    list = canvas.find_overlapping(0, 0, CANVAS_WIDTH, 30)

    for object in list:
        canvas.delete(object)
    if turns == 3:
        canvas.create_text(485, 33, font=("Small Fonts", 27), text="Tries Left: 2", fill="light grey")
        canvas.create_text(125, 30, font=("Small Fonts", 33), text="Breakout©", fill="light grey")
    if turns == 2:
        canvas.create_text(485, 33, font=("Small Fonts", 27), text="Tries Left: 1", fill="light grey")
        canvas.create_text(125, 30, font=("Small Fonts", 33), text="Breakout©", fill="light grey")
    if turns == 1:
        canvas.create_text(485, 33, font=("Small Fonts", 27), text="Tries Left: 0", fill="maroon")
        canvas.create_text(125, 30, font=("Small Fonts", 33), text="Breakout©", fill="light grey")



def lose_screen(canvas):

    canvas.create_text(300, 375, font=("Small Fonts", 27), text="You Lost! " + str(total_bricks(canvas)) + " bricks remaining.", fill="light grey")




def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1, bg="black")
    canvas.pack()
    return canvas



if __name__ == '__main__':
    main()
