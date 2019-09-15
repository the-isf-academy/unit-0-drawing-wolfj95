# Drawing project
# Author: Jacob Wolf

from helpers import no_delay
from base import draw_base, draw_cap
from turtle import hideturtle

def default_bottle_dimensions():
    return {
        'bottle_radius': 75,
        'bottle_height': 250,
        'lip_radius': 53,
        'taper_height': 10,
        'cap_radius': 50,
        'cap_height': 35,
        'handle_angle': 45,
        'bottle_rotation': 0,
        'depth': .2,
        'color': 'yellow'
    }

if __name__ == '__main__':
    dimensions = default_bottle_dimensions()
    with no_delay():
        draw_base(dimensions)
        draw_cap(dimensions)
        hideturtle()
    input("Press enter to continue...")
