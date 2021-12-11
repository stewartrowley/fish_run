import sys
from game.actor import Actor 
from game import constants
from game.point import Point
import raylibpy

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        pass
        
    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """

        # actor = Actor()

        dx = 0
        dy = 0

        if self.is_left_pressed():
            dx = -1
            # actor.set_image(constants.IMAGE_FISH_LEFT)
        
        if self.is_right_pressed():
            dx = 1
            # actor.set_image(constants.IMAGE_FISH)
        
        if self.is_up_pressed():
            dy = -1
            # actor.set_image(constants.IMAGE_FISH_TOP)
        
        if self.is_down_pressed():
            dy = 1
            # actor.set_image(constants.IMAGE_FISH_BOTTOM)

        direction = Point(dx, dy)
        return direction

    def is_left_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_LEFT)

    def is_right_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_RIGHT)

    def is_up_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_UP)

    def is_down_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_DOWN)

    def window_should_close(self):
        return raylibpy.window_should_close()