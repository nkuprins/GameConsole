from ponggame.world import World
from utility import Color, WIDTH, HEIGHT, SCALE

class View:

    def __init__(self, world, matrix):
    	self._world = world
        self._matrix = matrix
        self._draw_init()

    def _draw_init(self):
        # Draw background
        self._matrix.draw_background(Color.BLACK)
        # Draw border
        self._matrix.draw_border(Color.BLUE)
        # Draw platform
        self._matrix.draw_with_size(self._world.get_platform().get_pos(), Color.WHITE, 0, 3)
        # Draw ball
        self._matrix.draw_with_scale(self._world.get_ball().get_pos(), Color.WHITE)

    def draw_game(self, old_platform, old_ball):
        # Draw ball
        self._matrix.draw_with_scale(self._world.get_ball().get_pos(), Color.WHITE, old_ball, Color.BLACK)

        # Draw platform
        self._matrix.draw_with_size(self._world.get_platform().get_pos(), Color.WHITE, 0, 3, old_platform, Color.BLACK)
