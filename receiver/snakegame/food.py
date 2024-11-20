import random
from utility import SCALE, WIDTH

class Food:

    # (x, y) is the anchor point
    def __init__(self, x, y, world):
        self._x = x
        self._y = y
        self._world = world

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_pos(self):
        return (self._x, self._y)

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
