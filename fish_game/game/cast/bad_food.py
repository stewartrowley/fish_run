from game.actor import Actor
from game import constants

class BadFood(Actor):
    def __init__(self) -> None:
        super().__init__()
        self.set_width(constants.BAD_FOOD_WIDTH)
        self.set_height(constants.BAD_FOOD_HEIGHT)
