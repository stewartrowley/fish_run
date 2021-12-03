
from game.scoreboard import ScoreBoard
from game.action import Action
from game import constants
from game.shark import Shark
from game.point import Point

import random

class LevelUpActions(Action):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        pass
# #         # shark_list = []
# #         # for shark in cast['shark']:
# #         #     shark_list.append(shark)
# #         # food = cast['food']
# #         # if len(food) == 0:
# #         score_board = ScoreBoard()
# #         score = score_board.get_points()

        # shark_cast = cast['shark'] 
        # sharks = []
        # cast["shark"] = sharks      
        # for n in shark_cast:
        #     scoreboard = cast['scoreboard'][0]
        #     score = scoreboard.get_points()
        #     shark_num = Shark()
        #     x = random.randint(0, 0)
        #     y = random.randint(100, 500)
        #     if score >= 100:
        #         for i in range(2):
        #             position = Point(x, y)
        #             velocity_position = (Point((random.randint(1, constants.SHARK_DX) / 15), 0))
        #             shark_num.set_position(position)
        #             shark_num.set_velocity(velocity_position)
        #             sharks.append(shark_num)

            