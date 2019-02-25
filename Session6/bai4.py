from turtle import*
def draw_square(y, x):
    speed(0)
    color(x)
    forward(y)
    left(90)
for i in range(200):
    draw_square(i * 2, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()