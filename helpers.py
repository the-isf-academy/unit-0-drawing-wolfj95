# Helers
# Author: Chris Proctor

# This module is a collection of functions that might be useful in your drawing project.
# Some of these functions are probably a little too complicated for students to understand... yet!

from turtle import tracer, delay, update, position, heading, penup, pendown, setposition, setheading

class no_delay:
    """
    A context manager which runs drawing code instantly.
    """
    def __enter__(self):
        self.n = tracer()
        self.delay = delay()
        tracer(0, 0)

    def __exit__(self, exc_type, exc_value, traceback):
        update()
        tracer(self.n, self.delay)

class restore_state_when_finished:
    """
    A context manager which records the turtle's position and heading
    at the beginning and restores them at the end of the code block.
    For example:

        from turtle import forward, right
        from helpers import restore_state_when_finished

        for angle in range(0, 360, 15):
            with restore_state_when_finished():
                right(angle)
                forward(100)
    """

    def __enter__(self):
        self.position = position()
        self.heading = heading()

    def __exit__(self, *args):
        penup()
        setposition(self.position)
        setheading(self.heading)
        pendown()
