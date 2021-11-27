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
# from game.food import Food
# from game.scoreboard import Scoreboard
from game.control_actors_action import ControlActorsAction
# from game.handle_collisions_action import HandleCollisionsAction
# from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    sharks = []

    x = constants.SHARK_X 
    y = constants.SHARK_Y
    position = Point(x, y)
    velocity_position = (Point(constants.SHARK_DX, constants.SHARK_DY))
    shark = Shark()
    shark.set_position(position)
    shark.set_velocity(velocity_position)
    sharks.append(shark)

    cast["shark"] = [shark]

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
    

    cast["food"] = []
    # TODO: Create a paddle here and add it to the list

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    control_actors_action = ControlActorsAction(input_service)
    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action]
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