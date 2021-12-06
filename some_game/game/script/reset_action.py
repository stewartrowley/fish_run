
from game.action import Action
from game.cast.food import Food
from game.cast.bad_food import BadFood
from game.cast.shark import Shark
from game.point import Point
from game import constants
import random

class ResetAction(Action):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        if cast['food'] == []:

            # sharks = []
            # cast["shark"] = sharks
            # for n in range(random.randint(0, 5)):
            #     shark = Shark()
            #     x = random.randint(0, 0)
            #     y = random.randint(100, 500)
            #     position = Point(x, y)
            #     velocity_position = (Point((random.randint(1, constants.SHARK_DX) / 15), 0))
            #     shark.set_position(position)
            #     shark.set_velocity(velocity_position)
            #     sharks.append(shark)


            foods = []
            cast["food"] = foods
            for n in range(random.randint(1, constants.FOOD_SUPPLY)):
                x = random.randint(100, 700)
                y = random.randint(100, 550)
                position = Point(x, y)
                food = Food()
                # images = constants.IMAGE_FOOD
                # food.set_image(images)
                food.set_position(position)
                food_points = random.randint(1, 10)
                food.set_points(food_points)
                foods.append(food)
           

        if cast['bad_food'] == []:
            bad_foods =[]
            cast["bad_food"] = bad_foods
            for n in range(random.randint(1, constants.BAD_FOOD_SUPPLY)):
                x = random.randint(100, 700)
                y = random.randint(100, 550)
                position = Point(x, y)
                bad_food = BadFood()
                # images = constants.IMAGE_BAD_FOOD
                # bad_food.set_image(images)
                bad_food.set_position(position)
                bad_food_points = random.randint(-10, -1)
                bad_food.set_points(bad_food_points)
                # scored = bad_food.get_points()
                # bad_food.set_text(str(scored))
                bad_foods.append(bad_food)

        # sharks = []
        # cast["shark"] = sharks
        # scoreboard = cast['scoreboard'][0]
        # score = scoreboard.get_points()
        # if score == 0:
        #     for n in range(1):
        #         shark = Shark()
        #         x = random.randint(0, 0)
        #         y = random.randint(100, 500)
        #         position = Point(x, y)
        #         velocity_position = (Point((random.randint(1, constants.SHARK_DX) / 65), 0))
        #         shark.set_position(position)
        #         shark.set_velocity(velocity_position)
        #         sharks.append(shark)
        # if score >= 100:
        #     for n in range(2):
        #         shark = Shark()
        #         x = random.randint(0, 0)
        #         y = random.randint(100, 500)
        #         position = Point(x, y)
        #         velocity_position = (Point((random.randint(1, constants.SHARK_DX) / 15), 0))
        #         shark.set_position(position)
        #         shark.set_velocity(velocity_position)
        #         sharks.append(shark)
        # if score >= 200:
        #     for n in range(3):
        #         shark = Shark()
        #         x = random.randint(0, 0)
        #         y = random.randint(100, 500)
        #         position = Point(x, y)
        #         velocity_position = (Point((random.randint(1, constants.SHARK_DX) / 15), 0))
        #         shark.set_position(position)
        #         shark.set_velocity(velocity_position)
        #         sharks.append(shark)
        # if score >= 300:
        #     for n in range(4):
        #         shark = Shark()
        #         x = random.randint(0, 0)
        #         y = random.randint(100, 500)
        #         position = Point(x, y)
        #         velocity_position = (Point((random.randint(1, constants.SHARK_DX) / 15), 0))
        #         shark.set_position(position)
        #         shark.set_velocity(velocity_position)
        #         sharks.append(shark)            

        


        