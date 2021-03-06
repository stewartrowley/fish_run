from math import factorial
from os import remove
from typing import Collection
import random
from game.services.audio_service import AudioService
from game import constants
from game.cast.food import Food
from game.services.physics_service import PhysicsService
from game.point import Point
from game.action import Action
from game.cast.scoreboard import ScoreBoard
from game.actor import Actor

class HandleCollisionsAction(Action):
    def __init__(self) -> None:
        super().__init__()
        self._actor = Actor()

    def execute(self, cast):
        physics = PhysicsService()
        score_board = cast['scoreboard'][0]
        audio = AudioService()
   

        fish = cast['fish'][0]

        food_remove_list = []
        food_cast = cast['food']
        for foods in food_cast:
            collision = physics.is_collision(foods, fish)
            if collision == True:
                food_remove_list.append(foods)
                audio.play_sound(constants.SOUND_START)
                for food_num in food_remove_list:
                    if foods == food_num:
                        get_score = food_num.get_points()
                        food_cast.remove(food_num)
                        food_remove_list.remove(foods)
                        score_board.add_points(get_score)
                        print('true')
                        print(get_score)

        
        bad_food_remove_list = []
        bad_food_cast = cast['bad_food']
        for bad_foods in bad_food_cast:
            collision = physics.is_collision(bad_foods, fish)
            if collision == True:
                bad_food_remove_list.append(bad_foods)
                audio.play_sound(constants.SOUND_START)
            for bad_food_num in bad_food_remove_list:
                if bad_foods == bad_food_num:
                    score = bad_food_num.get_points()
                    score_board.add_points(score)
                    bad_food_cast.remove(bad_food_num)
                    print('true')
                    bad_food_remove_list.remove(bad_foods)


        cast_fish = cast['fish']
        for sharks in cast['shark']:
            # sharks = sharks
            remove_fishes = []
            cast_fish = cast['fish']
            for fish in cast_fish:
                collided = physics.is_collision(sharks, fish)
                if collided == True:
                    remove_fishes.append(fish)
                    for fish_num in remove_fishes:
                        cast_fish.remove(fish_num)
                        remove_fishes.remove(fish) 

 

        for octopus in cast['octopus']:
            for fish in cast['fish']:
                collided2 = physics.is_collision(octopus, fish)
                if collided2 == True:
                    get_score1 = octopus.get_points()
                    score_board.add_points(get_score1)
                    dx = octopus.get_velocity().get_x()
                    dy = octopus.get_velocity().get_y()
                    octopus.set_velocity(Point(dx, -dy))

                    






        # remove_all = []
        # fish_list = cast['fish']
        # for fishes in fish_list:
        #     collided = physics.is_collision(sharks, fishes)
        #     if collided == True:
        #         remove_all.append(fishes)           
        #         for fish_num in remove_all:
        #             if fishes == fish_num:
        #                 fish_list.remove(fish_num)
        #                 remove_all.remove(fishes)




                        
               
