from games.parent.world_parent import WorldParent

class WorldBorder(WorldParent):

    def __init__(self, background_color, border_color):
        super().__init__(background_color)
        self._border_color = border_color

    def get_border_color(self):
        return self._border_color
