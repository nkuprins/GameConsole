from cubesfallgame.world import World
from utility import Color, WIDTH, HEIGHT, SCALE

class View:

    def __init__(self, world, matrix):
    	self._world = world
        self._matrix = matrix
        self._draw_init()

    def _draw_init(self):
        # Draw background
        self._matrix.draw_background(Color.BLACK)
        # Draw cubes
        self._draw_cubes()

    def _draw_cubes(self):
        for cube in self._world.get_cubes():
            self._matrix.draw_pixel_(cube.get_pos(), cube.get_color())

    def draw_cube(self, cube, old_pos):
        self._matrix.draw_pixel_(cube.get_pos(), cube.get_color(), old_pos, Color.BLACK)

    def has_cube(self, pos):
        return !self._matrix.has_color(pos[0], pos[1], Color.BLACK)
