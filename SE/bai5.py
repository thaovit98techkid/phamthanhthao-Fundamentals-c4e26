from turtle import *
from random import choice
shape ("turtle")
speed (2)
right (60)
def daw_star(chieudai):
        for i in range (5):
                x = choice(["blue","black","green"])
                color (x) 
                forward (chieudai)
                right (144)
                               
daw_star(200)
mainloop ()