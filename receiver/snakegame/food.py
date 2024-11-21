from game.gameobject import GameObject
import random
from utility import SCALE, WIDTH

class Food(GameObject):

    # (x, y) is the anchor point
    def __init__(self, x, y, world):
        super().__init__(x, y, world)

    def _random_spawn_coord(self):
        return random.randint(SCALE + 1, WIDTH - 1 - SCALE)

    def random_spawn(self):
        new_x = self._x + 4 #self._random_spawn_coord()
        new_y = self._y     #self._random_spawn_coord()

        while self._world.get_snake().is_collided_with_snake(new_x, new_y):
            new_x = self._random_spawn_coord()
            new_y = self._random_spawn_coord()

        self._x = new_x
        self._y = new_y
