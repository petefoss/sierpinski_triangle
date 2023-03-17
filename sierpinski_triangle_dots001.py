from turtle import *
import turtle as t
from PIL import Image
import random
import time

start_time = time.time()

# Constants
#coords of triangle corners
top = [0, 348]
bottom_left= [-402, -402]
bottom_right = [402, -402]
list_corners = [top, bottom_left, bottom_right]
side_length = 804
num_dots = 10000

# This function is not used anymore because it slowed down the program so much (100 dots with make_mark() == 5 secs, but 1.8 secs without)
# this function shrinks the turtle size before stamping and then reverts to originall size - for a more pleasing visual.
def make_mark():
	turtlesize(0.1)
	stamp()
	turtlesize(1)

#draw triangle - This is an optional extra and doesn't currently run (It looks better without it)
def draw_triangle():
	pencolor("red")
	goto(bottom_left)
	pendown()
	goto(bottom_right)
	goto(top)
	goto(bottom_left)
	penup()

# Set the turtle settings
penup()
shape("circle")
pensize(10)
speed(0)    # speed '0' is the fastest
color("blue")
turtlesize(0.1)
# pencolor("red")


# start point
a = random.randint(-402, 402)
new_position = [a, -402]
goto(new_position)
stamp()

# Draw the triangle -  Loop 'num_dots' times
for i in range(num_dots):
	random_corner = random.randint(0, 2)
	temp_position = [0, 0]
	temp_position[0] =(new_position[0]+list_corners[random_corner][0])//2
	temp_position[1] =(new_position[1]+list_corners[random_corner][1])//2
	new_position = temp_position
	goto(new_position)
	stamp()

# draw_triangle()  # draws a red outline to the triangle

hideturtle()       # This hides the turtle before the image is saved

# this saves the canvas as a postscript vector file
canvas = t.getcanvas()
canvas.postscript(file='triangles.ps') 

# prints the time it takes to draw the triangle
print("--- %s seconds ---" % (time.time() - start_time))


done() # this keeps the turtle window open ofter completing the code (without this or similar the canvas just closes)


# times

# 10,000 dots takes 605 seconds

