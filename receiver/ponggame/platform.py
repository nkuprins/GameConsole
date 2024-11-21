from game.gameobject import GameObject
from utility import Direction, HEIGHT, SCALE

# Class that represents a platform
class Platform(GameObject):

    def __init__(self, x, y, world):
        super().__init__(x, y, world)

    def move(self, direction):
        if direction is None or \
            direction == Direction.LEFT or direction == Direction.RIGHT:
            return

        new_y = self._y + Direction.to_coord(direction)[1]
        self._y = min(max(new_y, SCALE + 1), HEIGHT - (SCALE + 1) * 2)
