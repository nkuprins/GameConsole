import random
from utility import BORDER_SIZE, SCALE

class Food:

    # (x, y) is a point that should be at the top-left corner of a food
    # Note, at the start of the game, if the world scale is set to 0,
    # this is the only point of the food
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

    def _random_int(self):
        return random.randint(BORDER_SIZE + 1 + SCALE, BORDER_SIZE + 1 + SCALE)

    def move(self):
        new_x = self._x + 4 #self._random_int()
        new_y = self._y#self._random_int()

        while self._world.get_snake().is_collided_with_snake(new_x, new_y):
            new_x = self._random_int()
            new_y = self._random_int()

        self._x = new_x
        self._y = new_y
