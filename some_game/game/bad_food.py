from game.actor import Actor
from game import constants

class BadFood(Actor):
    def __init__(self) -> None:
        super().__init__()
        self.set_width(constants.FOOD_WIDTH)
        self.set_height(constants.FOOD_HEIGHT)
