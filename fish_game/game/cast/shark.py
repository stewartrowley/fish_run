from game.actor import Actor
from game import constants
from game.point import Point
import random

class Shark(Actor):
    def __init__(self) -> None:
        super().__init__()

        self.set_width(constants.SHARK_WIDTH)
        self.set_height(constants.SHARK_HEIGHT)

    def make_shark(self):
        x = random.randint(0, 0)
        y = random.randint(100, 500)
        position = Point(x, y)
        velocity_position = (Point((random.randint(1, constants.SHARK_DX) / 15), 0))
        images = constants.IMAGE_SHARK
        self.set_image(images)
        self.set_position(position)
        self.set_velocity(velocity_position)