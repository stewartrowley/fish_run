from game.actor import Actor
from game import constants

class Fish(Actor):
    def __init__(self) -> None:
        super().__init__()

        self.set_height(constants.FISH_HEIGHT)
        self.set_width(constants.FISH_WIDTH)