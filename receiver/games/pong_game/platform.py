from game.gameobject import GameObject
from properties.constants import HEIGHT, WORLD_SIZE
from properties.direction import Direction


# Class that represents a platform
class Platform(GameObject):

    def __init__(self, x, y, world):
        super().__init__(x, y, world)

    def move(self, direction):
        if direction is None or \
            direction == Direction.UP or direction == Direction.DOWN:
            return

        new_dir = Direction.get_clock_dir(direction)
        new_y = self._y + Direction.to_speed(new_dir)[1]
        self._y = min(max(new_y, WORLD_SIZE + 1), HEIGHT - (WORLD_SIZE + 1) * 2)
