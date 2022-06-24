"""
Mac OS X must use tk version 8.6.7.  See project instructions on how to switch.
"""
from graphics import *
import time
import math

#user input for parameters
radius = float(input("Enter radius (a number between 10 and 20):\n"))
v_0 = float(input("Enter an initial speed (between 30 and 80):\n"))
angle = float(input("Enter a number for intial trajectory in degrees (10-90 degrees):\n"))
inc = float(input("Enter a value for the simulation time increment:\n"))

g = 9.8

#calculate window size
H = ((v_0 ** 2) / (2 * g)) * ((math.sin(math.radians(angle)) ** 2))
R = ((v_0 ** 2) / g) * (math.sin(math.radians(angle * 2)))

win_x = (R + (3 * radius))
win_y = (H + (3 * radius))

#calculate moves
T = ((2 * v_0) / g) * (math.sin(math.radians(angle)))#time
moves = math.floor(T / inc)

#print(T, moves)

#create window
x = 0
y = win_y
win = GraphWin('trajectory', win_x, win_y)
p1 = Point(x, y)

#draw circle
C = Circle(p1, radius)
C.setFill('Yellow')
C.draw(win)

#move ball
for i in range(moves):
    t = i * inc
    #new positions
    x2 = (v_0 * math.cos(math.radians(angle)) * t)
    y2 = win_y - (v_0 * math.sin(math.radians(angle)) * t - (0.5 * g * (t ** 2)))
    #diffrence between old and new
    dx = x2 - x
    dy = y2 - y 
    print('iteration {}, dx = {:.3f}, dy = {:.3f}'.format(i, dx, dy))#print information
    #move ball
    time.sleep(0.04)
    C.move(dx, dy)
    #reset initial positions
    x = x2
    y = y2
   

    

                                             

#Close after mouse click
try:
    win.getMouse()    
    win.close()
except:
    pass