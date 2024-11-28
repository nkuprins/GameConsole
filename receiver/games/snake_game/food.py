from games.parent.game_object import GameObject
from properties.constants import WORLD_SIZE, WIDTH, HEIGHT
import random

class Food(GameObject):

    # (x, y) is the anchor point
    def __init__(self, x, y, world):
        super().__init__(x, y, world)

    def _random_spawn_coord(self, limit):
        return random.randrange(WORLD_SIZE + 1, limit - 3 - WORLD_SIZE, 2)

    def random_spawn(self):
        new_x = self._random_spawn_coord(WIDTH)
        new_y = self._random_spawn_coord(HEIGHT)

        while self._world.get_snake().is_collided_with_snake(new_x, new_y):
            new_x = self._random_spawn_coord()
            new_y = self._random_spawn_coord()

        self._x = new_x
        self._y = new_y
