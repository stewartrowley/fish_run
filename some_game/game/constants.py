import os
import random
from random import randint

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_BRICK = os.path.join(os.getcwd(), "./batter/assets/brick-3.png")
IMAGE_PADDLE = os.path.join(os.getcwd(), "./batter/assets/bat.png")
IMAGE_BALL = os.path.join(os.getcwd(), "./batter/assets/ball.png")

SOUND_START = os.path.join(os.getcwd(), "./some_game/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./some_game/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./some_game/assets/over.wav")

SHARK_X = random.randint(50, MAX_X)
SHARK_Y = random.randint(50 ,MAX_Y)

SHARK_SUPPLY = 2

FISH_X = 400
FISH_Y = 575

SHARK_DX = 5
SHARK_DY = 5

LEVEL_ONE = 4
LEVEL_TWO = 6
LEVEL_THREE = 8

SCOREBOARD_WIDTH = 48
SCOREBOARD_HEIGHT = 24

FOOD_WIDTH = 24
FOOD_HEIGHT = 24

FOOD_SUPPLY = 10
BAD_FOOD_SUPPLY = 3
# FOOD_POINTS = random.randint(1, 60)

BRICK_SPACE = 5

FISH_SPEED = 15

FISH_WIDTH = 40
FISH_HEIGHT = 24

SHARK_WIDTH = 24
SHARK_HEIGHT = 24

VELOCITY_DX = .02
VELOCITY_DY = .02
