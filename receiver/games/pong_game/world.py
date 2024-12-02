from games.pong_game.platform import Platform
from games.pong_game.ball import Ball
from games.parent.world_border import WorldBorder
from properties.constants import HEIGHT, WORLD_SIZE
from properties.color import Color
from properties.direction import Direction

class World(WorldBorder):

    def __init__(self):
        super().__init__(Color.BLACK, Color.BLUE)
        platform_x = WORLD_SIZE + 5
        self._platform = Platform(platform_x, int(HEIGHT / 2), self)
        self._ball = Ball(platform_x + WORLD_SIZE + 1, int(HEIGHT / 2), self)

    def get_platform(self):
        return self._platform

    def get_ball(self):
        return self._ball

    def get_platform_color(self):
        return Color.WHITE

    def get_ball_color(self):
        return Color.WHITE

    def get_platform_draw_dir(self):
        return Direction.DOWN

    def get_platform_draw_size(self):
        return 3
