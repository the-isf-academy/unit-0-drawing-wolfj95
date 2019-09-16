from turtle import *
from drawing.shapes import add_perspective, square_with_points, fly
from math import sqrt, pow
from helpers import restore_state_when_finished

def draw_oval(a, b):
    points = []
    with restore_state_when_finished():
        enter_position = position()
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
    return(points)

def draw_cylinder(radius, height, depth, color):
    with restore_state_when_finished():
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
    return oval_points

def draw_taper(larger_oval, smaller_oval):
    with restore_state_when_finished():
        prev_smaller_oval_index = 0
        prev_smaller_oval_point = smaller_oval[prev_smaller_oval_index]
        larger_oval_index = 0
        for curr_smaller_oval_index in range(1, len(smaller_oval)):
            curr_smaller_oval_point = smaller_oval[curr_smaller_oval_index]
            while abs( (larger_oval_index/len(larger_oval)) - (prev_smaller_oval_index/len(smaller_oval)) ) < abs( (larger_oval_index/len(larger_oval)) - (curr_smaller_oval_index/len(smaller_oval)) ):
                fly(larger_oval[larger_oval_index][0],larger_oval[larger_oval_index][1])
                goto(prev_smaller_oval_point)
                larger_oval_index += 1

            prev_smaller_oval_point = curr_smaller_oval_point
            prev_smaller_oval_index = curr_smaller_oval_index

        for i in range(larger_oval_index, len(larger_oval)):
            fly(larger_oval[i][0], larger_oval[i][1])
            goto(prev_smaller_oval_point)


def draw_base(dimensions):
    top_cylinder_points = draw_cylinder(dimensions['bottle_radius'], dimensions['bottle_height'], dimensions['depth'], dimensions['color'])
    pencolor('gray')
    fly(0, dimensions['bottle_height']/2+dimensions['taper_height'])
    pensize(dimensions['lip_radius']-dimensions['cap_radius'])
    lip_points = draw_oval(dimensions['lip_radius'], (dimensions['lip_radius'])*dimensions['depth'])
    pensize(1)
    pencolor(dimensions['color'])
    draw_taper(top_cylinder_points, lip_points)

def draw_cap(dimensions):
    fly(0, dimensions['bottle_height']/2+dimensions['cap_height']/2+dimensions['taper_height'])
    draw_cylinder(dimensions['cap_radius'], dimensions['cap_height'], dimensions['depth'], 'black')
