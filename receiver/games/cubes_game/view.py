from games.parent.view_parent import ViewParent

class View(ViewParent):

    def __init__(self, world, matrix):
        super().__init__(world, matrix)
        self._draw_cubes()
        matrix.refresh()

    def _draw_cubes(self):
        for cube in self._world.get_cubes():
            self._matrix.draw_pixel(cube.get_x(), cube.get_y(), cube.get_color())

    def draw_cube(self, x, y, old_x, old_y, color):
        self._clear_pixel_at_pos(old_x, old_y)
        self._matrix.draw_pixel(x, y, color)

    def refresh_cubes(self):
        self._matrix.refresh()

    def has_cube(self, new_x, new_y):
        return not self._matrix.has_color(new_x, new_y, self._world.get_background_color())
