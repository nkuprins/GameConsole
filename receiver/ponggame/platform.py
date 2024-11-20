from utility import Direction, WIDTH, HEIGHT, SCALE

# Class that represents a platform
class Platform:

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

    def move(self, direction):
        if direction is None or \
            direction == Direction.UP or direction == Direction.DOWN: 
            return
        new_x = self._x + Direction.to_coord(self._direction)[0]

        if self._is_collided_with_side(new_x):
            return

        self._x = new_x

    def _is_collided_with_side(self, x):
        return x >= (self._world.get_width() - 1 - SCALE) or x <= SCALE