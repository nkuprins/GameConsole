from games.parent.view_object import ViewObject

class ViewBorder(ViewObject):

	def __init__(self, world, matrix):
		super().__init__(world, matrix)
        matrix.draw_border(world.get_border_color())