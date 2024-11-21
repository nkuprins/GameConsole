from utility import Direction, WIDTH, SCALE

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
            
        new_x = self._x + Direction.to_coord(direction)[0]
        self._x = min(max(new_x, SCALE), WIDTH - 1 - SCALE)