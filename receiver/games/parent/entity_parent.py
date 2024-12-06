from games.parent.pos import Pos


class EntityParent(Pos):

    def __init__(self, x, y, world):
        super().__init__(x, y)
        self._world = world
