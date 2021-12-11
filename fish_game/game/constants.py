import os
import random
from random import randint

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_BAD_FOOD = os.path.join(os.getcwd(), "./fish_game/assets/metal.png")
IMAGE_FOOD = os.path.join(os.getcwd(), "./fish_game/assets/shrimp.png")
IMAGE_FISH = os.path.join(os.getcwd(), "./fish_game/assets/fish.png")
IMAGE_FISH_LEFT = os.path.join(os.getcwd(), "./fish_game/assets/fish_left.png")
IMAGE_FISH_TOP = os.path.join(os.getcwd(), "./fish_game/assets/fish-top.png")
IMAGE_FISH_BOTTOM = os.path.join(os.getcwd(), "./fish_game/assets/fish-bottom.png")
IMAGE_SHARK = os.path.join(os.getcwd(), "./fish_game/assets/shark.png")
IMAGE_SHARK2 = os.path.join(os.getcwd(), "./fish_game/assets/shark2edit.png")
IMAGE_OCTOPUS = os.path.join(os.getcwd(), "./fish_game/assets/octopus.png")
IMAGE_BACKGROUND = os.path.join(os.getcwd(), "./fish_game/assets/ocean.png")

SOUND_START = os.path.join(os.getcwd(), "./fish_game/assets/mixkit-sea-water-splash.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./fish_game/assets/mixkit-sea-water-splash.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./fish_game/assets/mixkit-short-transition-sweep.wav")

SHARK_X = random.randint(50, MAX_X)
SHARK_Y = random.randint(50 ,MAX_Y)

SHARK_SUPPLY = 2

FISH_X = 400
FISH_Y = 525

SHARK_DX = 5
SHARK_DY = 5

LEVEL_ONE = 4
LEVEL_TWO = 6
LEVEL_THREE = 8

SCOREBOARD_WIDTH = 48
SCOREBOARD_HEIGHT = 24

FOOD_WIDTH = 12
FOOD_HEIGHT = 12

BAD_FOOD_WIDTH = 13
BAD_FOOD_HEIGHT = 13

FOOD_SUPPLY = 10
BAD_FOOD_SUPPLY = 3
# FOOD_POINTS = random.randint(1, 60)

BRICK_SPACE = 5

FISH_SPEED = 10

FISH_WIDTH = 40
FISH_HEIGHT = 24

SHARK_WIDTH = 24
SHARK_HEIGHT = 24

OCTOPUS_WIDTH = 28
OCTOPUS_HEIGHT = 28

SHARK_GENERATOR_NUM = 500
