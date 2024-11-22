from games.cubes_game.world import World
from properties.color import Color
from games.parent.view_object import ViewObject

class View(ViewObject):

    def __init__(self, world, matrix):
        super().__init__(world, matrix)
        # Draw cubes
        self._draw_cubes()

    def _draw_cubes(self):
        for cube in self._world.get_cubes():
            self._matrix.draw_pixel(cube.get_x(), cube.get_y(), cube.get_color())

    def draw_cube(self, cube, old_pos):
        # Clear cube
        self._clear_pixel_at_pos(old_pos[0], old_pos[1])
        # Draw cube
        self._matrix.draw_pixel(cube.get_x(), cube.get_y(), cube.get_color())

    def has_cube(self, pos):
        return not self._matrix.has_color(pos, self._world.get_background_color())
