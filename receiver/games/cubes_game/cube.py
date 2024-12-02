from games.parent.coords import Coords

class Cube(Coords):

    def __init__(self, x, y, color, world):
        super().__init__(x, y, world)
        self._color = color

    def get_color(self):
        return self._color

    def move(self, new_x, new_y):
        self._x = new_x
        self._y = new_y

    def try_accelerate(self, orientation_axis, speed):
        return speed * 2 if speed != 0 and self._world.should_accelerate(orientation_axis) else speed
