from game.actor import Actor
from game import constants

class Shark(Actor):
    def __init__(self) -> None:
        super().__init__()

        self.set_width(constants.SHARK_WIDTH)
        self.set_height(constants.SHARK_HEIGHT)

        