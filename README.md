# Breakout
In Breakout, the initial configuration of the world appears as shown on the right. The colored
rectangles in the top part of the screen are bricks, and the slightly larger rectangle at the
bottom is the paddle. The paddle is in a fixed position in the vertical dimension, but moves
back and forth across the screen along with the mouse until it reaches the edge of its space.



![Game shots](https://user-images.githubusercontent.com/119602009/211140511-3fda5836-c0c8-4aba-ad19-78d389203238.png)




A complete game consists of three turns. On each turn, a ball is launched from the center of
the window toward the bottom of the screen. That ball bounces off the paddle and the walls of 
the world, in accordance with the physical principle generally
expressed as "the angle of incidence equals the angle of reflection". Thus, after two bounces--one off
the paddle and one off the right wall--the ball has trajectory towards the bricks. The ball then collides with the bricks. When that happens, the ball bounces just as it does on any other collision, but the brick disappears. The second diagram shows what the game looks like after that collision
and after the player has moved the paddle to put it in line with the oncoming ball.



The play on a turn continues in this way until one of two conditions occurs:
 
 1. The ball hits the lower wall, which means that the player must have missed it with the
paddle. In this case, the turn ends and the next ball is served if the player has any turns
left. If not, the game ends in a loss for the player.
 
 
 2. The last brick is eliminated. In this case, the player wins, and the game ends
immediately.
