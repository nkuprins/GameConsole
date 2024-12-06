class ViewParent:
    def __init__(self, world, matrix, background_color):
        self._world = world
        self._matrix = matrix
        self._background_color = background_color
        matrix.draw_background(background_color)

    def _clear_pixel_at_pos(self, x, y):
        self._matrix.draw_pixel(x, y, self._background_color)

    def _clear_sq_at_pos(self, pos):
        self._matrix.draw_square(pos, self._background_color)

    def _clear_rct_at_pos(self, pos, squares_num, direction):
        self._matrix.draw_rectangle(pos, squares_num, self._background_color, direction)