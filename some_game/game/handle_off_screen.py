
from game import constants
from game.action import Action
from game.point import Point

class HandleOffScreenAction(Action):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        for shark in cast['shark']:
                x = shark.get_position().get_x()
                y = shark.get_position().get_x()
                dx = shark.get_velocity().get_x()
                dy = shark.get_velocity().get_y()

                if x > 780 or x < 0:
                        # shark.set_position(Point(-x, y))
                        shark.set_velocity(Point(-dx, dy))

                # if y > 450 or y < 0:
                #         shark.set_velocity(Point(dx, -dy))
            

        # physics = PhysicsService()


        # for fish in cast['fish']:
        #     x = fish.get_position().get_x()
        #     y = fish.get_position().get_y()

        #     collision = physics.is_collision(fish, )
        #     if collision == True:
        #         fish.set_position(10, 10)
                