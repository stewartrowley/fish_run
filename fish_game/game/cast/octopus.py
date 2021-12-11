from game.actor import Actor
from game import constants

class Octopus(Actor):
    def __init__(self) -> None:
        super().__init__()

        self.set_width(constants.OCTOPUS_WIDTH)
        self.set_height(constants.OCTOPUS_HEIGHT)
