"""
File: Breakout.py
----------------
Breakout is an arcade video game developed and published by Atari, Inc. It was designed
by Steve Wozniak, based on conceptualization from Nolan Bushnell and Steve Bristow who were influenced by the
seminal 1972 Atari arcade game, Pong. The look and feel of this game has been inspired heavily from when the game was
first released on May 13, 1976, with a slight modern touch added to it. This program was the Final Project of CS106A.
"""

import tkinter
import time


# How big is the playing area
CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 800     # Height of drawing canvas in pixels

# Constants for the bricks
N_ROWS = 8              # How many rows of bricks there are
N_COLS = 10             # How many columns of bricks there are
SPACING = 5             # How much space is there between each brick
BRICK_START_X = 5
BRICK_START_Y = 75      # The y coordinate of the top-most brick
BRICK_HEIGHT = 20       # How many pixels high is each brick
BRICK_WIDTH = int((CANVAS_WIDTH - (N_COLS+1) * SPACING) / N_COLS)  # converted to int as this evaluates a float
BALL_SIZE = 30
PADDLE_Y = CANVAS_HEIGHT - 40
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 20



def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Breakout', bg="black")
    create_bricks(canvas)
    turns = 3
    while turns != 0:
        turn_counter(canvas, turns)
        run_game(canvas)
        turns -= 1
    lose_screen(canvas)
    canvas.mainloop()
# main() creates a canvas, draws the bricks on this canvas and a variable turns is assigned the value 3. While turns
# is not 0, turn_counter(canvas, turns) mainly prints the logo "Breakout" and "Tries Left" on the canvas.
# run_game(canvas) draws the ball & paddle and runs an animation loop. If the lose condition is achieved in
# run_game(canvas), the function ends and turns is reduced by 1. The lose screen is then applied to the canvas.
# canvas.mainloop() aids in keeping the canvas running for the user to see.




def create_bricks(canvas):
    for row in range(N_ROWS):
        for col in range(N_COLS):
            draw_bricks(canvas, row, col)
# create_bricks(canvas) draws the bricks for with the specified N_ROWS & N_COLS using a nested loop, thus drawing each
# brick, by calling draw_bricks(canvas, row, col), using through every iteration of the loop.



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
# draw_bricks(canvas, row, col) assigns the start_x by adding the initial coordinate, BRICK_START_X, with
# (col * (SPACING + BRICK_WIDTH)). This expression offsets the initial coordinate by the total length
# of all the bricks that has already been drawn, including each spacing between. end_x is the addition of start_x
# with the BRICK_WIDTH, the ending coordinate of the brick. This concept applies for the y values too. Thus, going
# through each value of row & col, the bricks will be drawn at their respective locations. For the rows, in
# ascending value, the color of each brick is varied to mimic a rainbow effect, just like the original game.



def turn_counter(canvas, turns):
    list = canvas.find_overlapping(120, 25, CANVAS_WIDTH, 30)
    canvas.create_text(125, 30, font=("Small Fonts", 33), text="Breakout©", fill="light grey")

    for object in list:
        canvas.delete(object)
    if turns == 3:
        canvas.create_text(485, 33, font=("Small Fonts", 27), text="Tries Left: 2", fill="light grey")

    if turns == 2:
        canvas.create_text(485, 33, font=("Small Fonts", 27), text="Tries Left: 1", fill="light grey")

    if turns == 1:
        canvas.create_text(485, 33, font=("Small Fonts", 27), text="Tries Left: 0", fill="maroon")
# turn_counter(canvas, turns) finds all the object bounded by an area of a rectangle in the top right quarter of
# the canvas. Then, the for loop goes through every object in that list and deletes the object(clearing the text that
# was previously there). Thus, for the first turn the "Tries Left" text is drawn, and for subsequent turns it is
# then deleted, and then updated (re-drawn with current number of Tries Left) each turn.




def run_game(canvas):
    ball = canvas.create_oval(275, 375, (275 + BALL_SIZE), (375 + BALL_SIZE), fill="firebrick3")
    dx = 10
    dy = 10
    paddle = canvas.create_rectangle(275, PADDLE_Y, (275 + PADDLE_WIDTH), (PADDLE_Y + PADDLE_HEIGHT), fill="firebrick3")
    top_border = canvas.create_line(0, 65, CANVAS_WIDTH, 65, fill="light grey")


    while True:
        bricks_left = total_bricks(canvas)  # int value of total bricks left

        canvas.move(ball, dx, dy)  # moves the ball by dx & dy each frame

        mouse_x = canvas.winfo_pointerx()  # returns the x-coordinate of the users mouse

        if 0 <= mouse_x <= 520:
            canvas.moveto(paddle, mouse_x, PADDLE_Y)
# Moves the paddle to mouse_x (changing) and PADDLE_Y (fixed) for the given range of mouse_x, otherwise the paddle will
# appear to move out of the canvas (the coordinates used are the top-left of the paddle).


        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            dx *= -1
# Ff the ball hits the left or right wall, the dx is then multiplied by -1, inverting its x-direction (bounce effect).


        if hit_bottom_wall(canvas, ball):
            canvas.delete(ball)
            canvas.delete(paddle)
            break
# if the ball hits the bottom wall, the animation loop is broken and run_game(canvas) ends. The ball & paddle is
# deleted. run_game(canvas), provided the turns is not 0.


        if bricks_left == 0:
            canvas.delete(ball)
            canvas.delete(paddle)
            canvas.create_text(300, 375, font=("Small Fonts", 33), text="You Won !", fill="light grey")
            canvas.mainloop()
# If the bricks left is 0, the game is won and the paddle and ball is then deleted. The text "You Won !" is displayed
# in the centre of the screen. canvas.mainloop() ensures that the canvas remains for the user to see the win screen.


        colliding_list = get_coords_list(canvas, ball)

        if len(colliding_list) > 1:
            dy *= -1
            for object in colliding_list:
                if object != ball and object != paddle and object != top_border:
                    canvas.delete(object)
# get_coords_list(canvas, ball) returns a list of all the object the ball is colliding with (if any). If the length of
# the list is greater than 1, dy is multiplied by -1 to invert its y-direction (bounce effect). If the object is
# colliding with is a brick (not ball, paddle or top_border), it is deleted.


        canvas.update()
        time.sleep(1/30)
# run_game(canvas) first creates a circle and assigns it to the variable ball. The variables dx & dy are the change in
# x and y of the ball. A rectangle is then created and assigned to the variable paddle. Another line is also
# created, which is then assigned to the variable top_border. An animation loop occurs, using the above variables.
# canvas.update() and time.sleep(1/30) updates the frame and the game runs at 30fps respectively.




def total_bricks(canvas):
    list = canvas.find_overlapping(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT)
    return (len(list) - 5)
# total_bricks(canvas) returns the length of the list of all the objects in the canvas, subtracting 5 objects (objects
# that are not bricks).



def hit_left_wall(canvas, ball):
    x_coordinate = get_left_x(canvas, ball)
    return x_coordinate <= 0

def hit_right_wall(canvas, ball):
    x_coordinate = get_left_x(canvas, ball) + BALL_SIZE
    return x_coordinate >= CANVAS_WIDTH

def hit_bottom_wall(canvas, ball):
    y_coordinate = get_top_y(canvas, ball) + BALL_SIZE
    return y_coordinate >= CANVAS_HEIGHT
# hit_wall(canvas,ball) gets the coordinate, and returns a boolean determining whether it has collided with the wall
# by comparing the coordinate with the x/y-coordinate of the respective wall.



def get_coords_list(canvas, ball):
    ball_coords = canvas.coords(ball)
    x_1 = ball_coords[0]
    y_1 = ball_coords[1]
    x_2 = ball_coords[2]
    y_2 = ball_coords[3]
    return canvas.find_overlapping(x_1, y_1, x_2, y_2)
# get_coords_list(canvas, ball) first assigns the list of the ball's coordinates to ball_coords. (x1, y1) is the
# top-left and (x2, y2) is the top-right. A list of all the objects within these bounds is then returned (objects
# colliding with the ball).



def get_left_x(canvas, object):
    return canvas.coords(object)[0]


def get_top_y(canvas, object):
    return canvas.coords(object)[1]
# get_x/y(canvas, object) returns the coordinate of the left side x-coordinate of the ball and top y-coordinate of
# the ball.



def lose_screen(canvas):
    canvas.create_text(300, 375, font=("Small Fonts", 27), text="You Lost! " + str(total_bricks(canvas)) + " bricks remaining.", fill="light grey")
# lose_screen(canvas) displays a text of "You Lost!" and how many bricks were remaining.



def make_canvas(width, height, title, bg):
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
