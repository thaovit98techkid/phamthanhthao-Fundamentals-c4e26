from turtle import *
from random import choice 
shape("turtle")
speed (2)
# mausac = choice(["red","pink","green","blue"])
# print (mausac)
def draw_sapes(chieudai,mausac):
    for i in range (4):
        color(mausac)
        forward (chieudai)
        right (90)
draw_sapes(200,"blue")
mainloop ()