import turtle

import colorgram
import turtle as t
import random


def extract_colors(no_of_colors):
    rgb_colors = []
    colors = colorgram.extract('image.jpeg', no_of_colors)
    for color in colors:
        color_space_tuple = ()
        for color_space in color.rgb:
            color_space_tuple += (color_space,)

        # check if r, g, b values are all < 240, if yes then append to list
        if all(c < 240 for c in color_space_tuple):
            rgb_colors.append(color_space_tuple)
    return rgb_colors


color_list = extract_colors(30)
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup() # remove the path line
tim.hideturtle()

# set the heading to start from bottom of the screen
tim.setheading(225)
tim.forward(550)
tim.setheading(0)


def gen_hirst_painting(no_of_dots, dots_per_row):
    for dot_count in range(1, no_of_dots + 1):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

        if dot_count % dots_per_row == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(dots_per_row*50)
            tim.setheading(0)


gen_hirst_painting(80, 10)

screen = turtle.Screen()
screen.exitonclick()

