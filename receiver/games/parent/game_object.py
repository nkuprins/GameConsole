from properties.constants import WORLD_SIZE
from games.parent.pos_object import PosObject

class GameObject(PosObject):

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

    # True if pos_a is collided with pos_b
    def _is_collided(self, pos_a, pos_b):
        a_start_x = pos_a[0]
        a_start_y = pos_a[1]
        a_end_x = pos_a[0] + WORLD_SIZE
        a_end_y = pos_a[1] + WORLD_SIZE
        b_start_x = pos_b[0]
        b_start_y = pos_b[1]
        b_end_x = pos_b[0] + WORLD_SIZE
        b_end_y = pos_b[1] + WORLD_SIZE

        return a_end_x >= b_start_x and a_start_x <= b_end_x and \
                a_end_y >= b_start_y and a_start_y <= b_end_y
