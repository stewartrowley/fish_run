import os
os.environ['RAYLIB_BIN_PATH'] = r'C:\Users\StewM\Documents\BYU Idaho\Fall 2021\programmingCourses\CSE210_personal\cseFinalProject\fish_run\some_game\raylib-2.0.0-Win64-mingw\lib'


from game.script.move_actors_action import MoveActorsAction
from game.script.level_up_action import LevelUpActions
from game.script.reset_action import ResetAction
from game.script.handle_collisions_action import HandleCollisionsAction
from game.script.handle_off_screen_action import HandleOffScreenAction
from game.script.control_actors_action import ControlActorsAction
from game.script.draw_actors_action import DrawActorsAction

from game.cast.octopus import Octopus
from game.cast.scoreboard import ScoreBoard
from game.cast.bad_food import BadFood
from game.cast.food import Food
from game.cast.shark import Shark
from game.cast.fish import Fish

from game.services.audio_service import AudioService
from game.services.physics_service import PhysicsService
from game.services.output_service import OutputService
from game.services.input_service import InputService

from game.point import Point
from game.actor import Actor
from game.director import Director
from game import constants
import random


# TODO: Add imports similar to the following when you create these classes


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    fishes = []

    x = constants.FISH_X
    y = constants.FISH_Y
    position = Point(x, y)
    fish = Fish()
    velocity = Point(0, 0)
    # image = constants.IMAGE_FISH
    # fish.set_image(image)
    fish.set_velocity(velocity)
    fish.set_position(position)
    fishes.append(fish)

    cast["fish"] = [fish]

    bad_foods = []
    for n in range(0, constants.BAD_FOOD_SUPPLY, 50):
        x = random.randint(100, 750)
        y = random.randint(100, 500)
        position = Point(x, y)
        bad_food = BadFood()
        bad_food.set_position(position)
        bad_food_points = random.randint(-10, -1)
        # images = constants.IMAGE_BAD_FOOD
        # bad_food.set_image(images)
        bad_food.set_points(bad_food_points)
        bad_foods.append(bad_food)

    cast["bad_food"] = bad_foods

    foods = []
    cast["food"] = foods
    for n in range(constants.FOOD_SUPPLY):
        x = random.randint(100, 750)
        y = random.randint(100, 500)
        position = Point(x, y)
        food = Food()
        food.set_position(position)
        food_points = random.randint(1, 10)
        # images = constants.IMAGE_FOOD
        # food.set_image(images)
        food.set_points(food_points)
        foods.append(food)

    sharks = []
    cast["shark"] = sharks
    for n in range(3):
        shark = Shark()
        x = random.randint(0, 0)
        y = random.randint(100, 500)
        position = Point(x, y)
        velocity_position = (Point((random.randint(1, constants.SHARK_DX) / 15), 0))
        # images = constants.IMAGE_SHARK
        # shark.set_image(images)
        shark.set_position(position)
        shark.set_velocity(velocity_position)
        sharks.append(shark)

    octopuses = []
    cast["octopus"] = octopuses
    for n in range(2):
        octopus = Octopus()
        x = random.randint(100, 500)
        y = random.randint(0, 0)
        position = Point(x, y)
        velocity_position = (Point(0, (random.randint(1, constants.SHARK_DX) / 5)))
        # images = constants.IMAGE_OCTOPUS
        octopus_points = -1
        octopus.set_points(octopus_points)
        # octopus.set_image(images)
        octopus.set_position(position)
        octopus.set_velocity(velocity_position)
        octopuses.append(octopus)

    scoreboards = []
    position = Point(1, 0)
    scoreboard = ScoreBoard()
    scoreboard.set_position(position)
    # total = scoreboard.get_points()
    # scoreboard.set_text(f'Score: {total}')
    scoreboards.append(scoreboard)
    cast["scoreboard"] = [scoreboard]

    # TODO: Create a paddle here and add it to the list

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    control_actors_action = ControlActorsAction(input_service)
    reset_action = ResetAction()
    handle_off_screen = HandleOffScreenAction()
    level_up_action = LevelUpActions()
    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action,
                        reset_action, level_up_action, handle_off_screen]
    script["output"] = [draw_actors_action]

    # Start the game
    output_service.open_window("Fish Run")
    audio_service.start_audio()
    # audio_service.play_sound(constants.SOUND_START)

    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()


if __name__ == "__main__":
    main()
