# Drawing project
# Author: Jacob Wolf

from helpers import no_delay
from base import draw_base, draw_cap
from turtle import hideturtle

def default_bottle_dimensions():
    """
    Returns a dictionary containing key-value pairs for the drawing settings for my water bottle.
    height and radius values are in standard Turtle units
    angle values are in degrees
    rotation values are values between 0 and 1 representing the rotation of the bottle around an axis
    color is a color value used by the Turtle pen
    """
    return {
        'bottle_radius': 75.5,
        'bottle_height': 325,
        'lip_radius': 53,
        'taper_height': 15,
        'cap_radius': 50,
        'cap_height': 40,
        'handle_angle': 45,
        'y_rotation': 0,
        'x_rotation': .2,
        'color': 'yellow'
    }

if __name__ == '__main__':
    """
    Draws the bottle by calling functions from the base module using the no_delay context manage from the helpers module
    """
    dimensions = default_bottle_dimensions()
    with no_delay():
        draw_base(dimensions)
        draw_cap(dimensions)
        hideturtle()
    input("Press enter to continue...")
