
class ViewObject:

	def __init__(self, world, matrix):
		self._world = world
        self._matrix = matrix
        matrix.draw_background(world.get_background_color())

    def _clear_pixel_at_pos(self, x, y):
        self._matrix.draw_pixel(x, y, self._world.get_background_color())

    def _clear_sq_at_pos(self, pos):
    	self._matrix.draw_square(pos, self._world.get_background_color())

    def _clear_rct_at_pos(self, pos, squares_num, direction):
        self._matrix.draw_rectangle(pos, 3, self._world.get_background_color(), direction)