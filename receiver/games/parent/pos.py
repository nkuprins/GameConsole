from games.parent.coords import Coords

class Pos(Coords):

    def __init__(self, x, y, world):
        super().__init__(x, y, world)

    def get_pos(self):
        return self._x, self._y