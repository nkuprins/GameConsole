class GameParent:
    def __init__(self, world, view):
        self._world = world
        self._view = view

    def get_world(self):
        return self._world

    def get_view(self):
        return self._view
