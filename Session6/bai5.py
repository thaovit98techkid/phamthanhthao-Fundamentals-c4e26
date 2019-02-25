from turtle import *
from random import choice
shape ("turtle")
speed (2)
def daw_star(x,y,chieudai):
        goto(x,y)
        for i in range (5):
                x = choice(["blue","black","green"])
                color (x) 
                forward (chieudai)
                right (144)
                               
daw_star(0,0,200)
mainloop ()
