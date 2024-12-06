from games.parent.world_parent import WorldParent
from games.pong_game.ball import Ball
from games.pong_game.platform import Platform
from properties.constants import HEIGHT, WORLD_SIZE

class World(WorldParent):

    def __init__(self):
        super().__init__()
        platform_x = WORLD_SIZE + 5
        self._platform = Platform(platform_x, int(HEIGHT / 2), self)
        self._ball = Ball(platform_x + WORLD_SIZE + 1, int(HEIGHT / 2), self)

    def get_platform(self):
        return self._platform

    def get_ball(self):
        return self._ball