import random
from utility import Direction, WIDTH, HEIGHT, SCALE, CUBES_SENSITIVITY

# Class that represents a cube
class Cube:

    # (x, y) is the anchor point
    def __init__(self, x, y, color, world):
        self._x = x
        self._y = y
        self._world = world
        self._color = color

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_pos(self):
        return (self._x, self._y)

    def get_color(self):
        return self._color

    def move(self, pos):
        self._x = pos[0]
        self._y = pos[1]

    def get_move_coord(self, orientation):
        coord = self._get_speed_coord(orientation)

        if coord[0] == 0 and coord[1] == 0:
            return None

        new_coord = self._accelerate_coord(orientation)

        new_x = min(max(self._x + new_coord[0], 0), WIDTH - 1)
        new_y = min(max(self._y + new_coord[1], 0), HEIGHT - 1)
        return [new_x, new_y]

    def _get_speed_coord(orientation):
        def calculate(coord):
            if coord > CUBES_SENSITIVITY: return 1
            elif coord < -CUBES_SENSITIVITY: return -1
            else return 0

        return [calculate(orientation[0]), calculate(orientation[1])]

    def _accelerate_coord(orientation):
        new_coord_x = self._random_accelerate(orientation[0]) ? coord[0] * 2 : coord[0]
        new_coord_y = self._random_accelerate(orientation[1]) ? coord[1] * 2 : coord[1]
        return [new_coord_x, new_coord_y]

    def _random_accelerate(orientation):
        probability = min(max(0.006 * abs(orientation), 0), 1)
        return (random.randint(0, 100) / 100) < probability