from games.parent.view_parent import ViewParent

class ViewBorder(ViewParent):

    def __init__(self, world, matrix):
        super().__init__(world, matrix)
        matrix.draw_border(world.get_border_color())
