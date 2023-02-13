# Breakout
In Breakout, the initial configuration of the world appears as shown on the right (Start of Breakout). The colored
rectangles in the top part of the screen are bricks, and the slightly larger rectangle at the
bottom is the paddle. The paddle is in a fixed position in the vertical dimension, but moves
back and forth across the screen along with the mouse until it reaches the edge of its space.
The look of the game was heavily inspired from the [software version of Breakout](https://en.wikipedia.org/wiki/Breakout_%28video_game%29#/media/File:Breakout2600.svg) which was written for the Atari® 2600 in 1978 with a slight modern touch added to it.




![Game shots](https://user-images.githubusercontent.com/119602009/211180394-bede9e50-5c08-46da-b1aa-f3c7e8099d15.png)




A complete game consists of three turns. On each turn, a ball is launched from the centre of
the window toward the bottom of the screen. This ball bounces off the paddle and the walls of 
the world, in accordance with the physical principle generally expressed as "the angle of 
incidence equals the angle of reflection". Thus, after two bounces--one off the paddle and one 
off the right wall--the ball has a trajectory towards the bricks. The ball then collides with 
the bricks. When that happens, the ball bounces just as it does on any other collision, but the 
bricks disappears. The second diagram shows what the game looks like after this collision and
after the player has moved the paddle to put it in line with the oncoming ball (Gameplay screenshot of Breakout).



The play on a turn continues in this way until one of two conditions occurs:
 
 1. The ball hits the lower wall, meaning that the player must have missed it with the
paddle. In this case, the turn ends and the next ball is served if the player has any turns
left. If not, the game ends in a loss for the player ("Lose" screen).
 
 
 2. The last brick is eliminated. In this case, the player wins, and the game ends
immediately ("Win" screen). 


-----------------------------------------------------------------------------------------------
This program was a blast to write. Applying the concept of decompostion by breaking the program 
down into smaller problems and tackling them individually was key. I have learnt a lot from 
CS106A and this project is a testament of what I have gained so far. 


Here are some documents on how to get this program running (do note to open the folder breakout.py is directly in, "Breakout Game", when in PyCharm):

[Get Pycharm.pdf](https://github.com/omcodedthis/Breakout/files/10365789/Get.Pycharm.pdf)

[Graphics (Tkinter) reference.pdf](https://github.com/omcodedthis/Breakout/files/10365896/Graphics.Tkinter.reference.pdf)
