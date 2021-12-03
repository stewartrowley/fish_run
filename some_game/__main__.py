import os
os.environ['RAYLIB_BIN_PATH'] = r'C:\Users\StewM\Documents\BYU Idaho\Fall 2021\programmingCourses\CSE210_personal\cseFinalProject\fish_run\some_game\raylib-2.0.0-Win64-mingw\lib'

import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.fish import Fish
from game.shark import Shark
from game.food import Food
from game.bad_food import BadFood
from game.scoreboard import ScoreBoard
from game.control_actors_action import ControlActorsAction
from game.handle_off_screen import HandleOffScreenAction
from game.handle_collisions_action import HandleCollisionsAction
from game.reset_action import ResetAction
from game.level_up_action import LevelUpActions
from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}


    fishes = []
    
    x = constants.FISH_X
    y = constants.FISH_Y
    position = Point(x, y)
    fish = Fish()
    velocity = Point(0, 0)
    fish.set_velocity(velocity)
    fish.set_position(position)
    fishes.append(fish)

    cast["fish"] = [fish]

    bad_foods =[]
    for n in range(0, constants.BAD_FOOD_SUPPLY, 50):
        x = random.randint(100, 750)
        y = random.randint(100, 500)
        position = Point(x, y)
        bad_food = BadFood()
        bad_food.set_position(position)
        bad_food_points = random.randint(-10, -1)
        bad_food.set_points(bad_food_points)
        scored = bad_food.get_points()
        bad_food.set_text(str(scored))
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
        food.set_points(food_points)
        scored = food.get_points()
        food.set_text(str(scored))
        foods.append(food)

    sharks = []
    cast["shark"] = sharks
    for n in range(8):
        shark = Shark()
        x = random.randint(0, 0)
        y = random.randint(100, 500)
        position = Point(x, y)
        velocity_position = (Point((random.randint(1, constants.SHARK_DX) / 15), 0))
        shark.set_position(position)
        shark.set_velocity(velocity_position)
        sharks.append(shark)




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
    script["update"] = [move_actors_action, handle_collisions_action, reset_action, handle_off_screen, level_up_action]
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