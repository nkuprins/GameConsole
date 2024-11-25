from games.cubes_game.world import World
from properties.color import Color
from games.parent.view_object import ViewObject

class View(ViewObject):

    def __init__(self, world, matrix):
        super().__init__(world, matrix)
        # Draw cubes
        self._draw_cubes()
        matrix.refresh()

    def _draw_cubes(self):
        for cube in self._world.get_cubes():
            self._matrix.draw_pixel(cube.get_x(), cube.get_y(), cube.get_color())

    def draw_cube(self, x, y, old_x):
        # Clear cube
        self._clear_pixel_at_pos(old_x, old_y)
        # Draw cube
        self._matrix.draw_pixel(x, y, cube.get_color())

    def refresh_cubes(self):
        self._matrix.refresh()

    def has_cube(self, new_x, new_y):
        return not self._matrix.has_color(new_x, new_y, self._world.get_background_color())
