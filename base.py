from turtle import *
from drawing.shapes import add_perspective, square_with_points, fly
from math import sqrt, pow

def draw_oval(a, b):
    points = []
    enter_position = position()
    enter_heading = heading()
    fly(enter_position[0]-(a), enter_position[1])
    points.append(position())
    for x in range(int(enter_position[0]-a), int(enter_position[0]+a)):
        y = sqrt(pow(b,2)-pow((x-enter_position[0])*b/a, 2)) + enter_position[1]
        goto(x, y)
        points.append(position())
    for x in range(int(enter_position[0]+a), int(enter_position[0]-a), -1):
        y = -(sqrt(pow(b,2)-pow((x-enter_position[0])*b/a, 2))) + enter_position[1]
        goto(x, y)
        points.append(position())
    goto(enter_position[0]-(a), enter_position[1])
    points.append(position())
    fly(enter_position[0], enter_position[1])
    setheading(enter_heading)
    return(points)

def draw_cylinder(radius, height, depth, color):
    enter_heading = heading()
    penup()
    setheading(270)
    forward(height/2)
    pendown()
    pencolor('gray')
    draw_oval(radius, radius*depth)
    penup()
    setheading(90)
    forward(height)
    pendown()
    pencolor(color)
    oval_points = draw_oval(radius, radius*depth)
    add_perspective(oval_points, [0, 100*height], -.01)
    pencolor('gray')
    draw_oval(radius, (radius)*depth)
    penup()
    setheading(270)
    forward(height/2)
    setheading(enter_heading)


def draw_base(dimensions):
    draw_cylinder(dimensions['bottle_radius'], dimensions['bottle_height'], dimensions['depth'], dimensions['color'])
    pencolor('gray')
    fly(0, dimensions['bottle_height']/2+dimensions['taper_height'])
    pensize(dimensions['lip_radius']-dimensions['cap_radius'])
    draw_oval(dimensions['lip_radius'], (dimensions['lip_radius'])*dimensions['depth'])
    pensize(1)

def draw_cap(dimensions):
    fly(0, dimensions['bottle_height']/2+dimensions['cap_height']/2+dimensions['taper_height'])
    draw_cylinder(dimensions['cap_radius'], dimensions['cap_height'], dimensions['depth'], 'black')
