from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]

def get_shapes():
    return shapes

def generate_quiz():
    index1 = randint(0,3)
    index2 = randint(0,3)
    text = shapes[index1]["text"]
    color = shapes[index2]["color"]
    return [
                text,
                color,
                randint(0, 1) # 0 : meaning duoi, 1: color tren
            ]

def mouse_press(x, y, text, color, quiz_type):
    green = shapes[3]
    rect_green = green["rect"]

    red = shapes[1]
    rect_red = red["rect"]

    yellow = shapes[2]
    rect_yellow = yellow["rect"]

    blue = shapes[0]
    rect_blue = blue["rect"]

    print (x, y, text, color, quiz_type)


    if quiz_type == 1:
        if color ==  "#C62828": #do
            if x < rect_red[0] or y < rect_red[1] or  x > rect_red[3] + rect_red[0] or x > rect_red[1] + rect_red[2]:
                kqua = False      
            else :
                kqua = True
        elif color == '#3F51B5': #blue
            if x < rect_blue[0] or y < rect_blue[1] or  x > rect_blue[3] + rect_blue[0] or x > rect_blue[1] + rect_blue[2]:
                kqua = False      
            else :
                kqua = True
        elif color == '#FFD600': #vang
            if x < rect_yellow[0] or y < rect_yellow[1] or  x > rect_yellow[3] + rect_yellow[0] or x > rect_yellow[1] + rect_yellow[2]:
                kqua = False      
            else :
                kqua = True
        elif color == '#4CAF50': #green
            if x < rect_green[0] or y < rect_green[1] or  x > rect_green[3] + rect_green[0] or x > rect_green[1] + rect_green[2]:
                kqua = False      
            else :
                kqua = True
    else :
        if text ==  "red": #do
            if x < rect_red[0] or y < rect_red[1] or  x > rect_red[3] + rect_red[0] or x > rect_red[1] + rect_red[2]:
                kqua = False      
            else :
                kqua = True
        elif text == 'blue': #blue
            if x < rect_blue[0] or y < rect_blue[1] or  x > rect_blue[3] + rect_blue[0] or x > rect_blue[1] + rect_blue[2]:
                kqua = False      
            else :
                kqua = True
        elif text == 'yellow': #vang
            if x < rect_yellow[0] or y < rect_yellow[1] or  x > rect_yellow[3] + rect_yellow[0] or x > rect_yellow[1] + rect_yellow[2]:
                kqua = False      
            else :
                kqua = True
        elif text == 'green': #green
            if x < rect_green[0] or y < rect_green[1] or  x > rect_green[3] + rect_green[0] or x > rect_green[1] + rect_green[2]:
                kqua = False      
            else :
                kqua = True      
    return kqua