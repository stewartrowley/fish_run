
from datetime import datetime
from game.cast.scoreboard import ScoreBoard
from game.action import Action
from game import constants
from game.cast.shark import Shark
from game.point import Point

import random

class LevelUpActions(Action):
    def __init__(self) -> None:
        super().__init__()

        self.i = 0

    def execute(self, cast):   

        self.i += 1
        if self.i % constants.SHARK_GENERATOR_NUM == 0:

            sharks = cast['shark']
            for n in range(2):
                shark = Shark()
                shark.make_shark()
                sharks.append(shark)



        # time_list = []
        # for n in range(1):
        #     now = datetime.now()

        #     current_time = now.strftime("%M")
        #     time_list.append(current_time)            

        # for time in time_list:
        #     now = datetime.now()
        #     future_time = now.strftime("%M")
        #     if future_time == time:
        #         sharks = []
        #         for n in range(2):
        #             shark = Shark()
        #             shark.make_shark()
        #             sharks.append(shark)
        #         cast['shark'] = sharks


        #     shark_list = []
        #     for n in cast_shark:
        #         shark_list.append(n)
        #         for i in shark_list:
        #             if i == n:
        #                 cast_shark.remove(i)
        #             sharks = []
        #             cast["shark"] = sharks
        #             for n in range(2):
        #                 shark = Shark()
        #                 x = random.randint(100, 500)
        #                 y = random.randint(0, 0)
        #                 position = Point(x, y)
        #                 velocity_position = (Point((random.randint(1, constants.SHARK_DX) / 600), 0))
        #                 images = constants.IMAGE_SHARK
        #                 shark.set_image(images)
        #                 shark.set_position(position)
        #                 shark.set_velocity(velocity_position)
        #                 sharks.append(shark)

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

            