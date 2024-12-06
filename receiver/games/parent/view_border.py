from games.parent.view_parent import ViewParent

class ViewBorder(ViewParent):

    def __init__(self, world, matrix, background_color, border_color):
        super().__init__(world, matrix, background_color)
        matrix.draw_border(border_color)
        self._border_color = border_color