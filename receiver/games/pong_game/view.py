from games.parent.view_border import ViewBorder

class View(ViewBorder):

    def __init__(self, world, matrix):
        super().__init__(world, matrix)
        # Draw platform
        matrix.draw_rectangle(
            world.get_platform().get_pos(),
            world.get_platform_draw_size(),
            world.get_platform_color(),
            world.get_platform_draw_dir()
        )
        # Draw ball
        matrix.draw_square(world.get_ball().get_pos(), world.get_ball_color())
        matrix.refresh()

    def draw_game(self, old_platform, old_ball):
        w = self._world
        m = self._matrix

        # Clear ball
        self._clear_sq_at_pos(old_ball)
        # Draw ball
        m.draw_square(w.get_ball().get_pos(), w.get_ball_color())

        # Clear platform
        self._clear_rct_at_pos(old_platform, w.get_platform_draw_size(), w.get_platform_draw_dir())
        # Draw platform
        m.draw_rectangle(
            w.get_platform().get_pos(),
            w.get_platform_draw_size(),
            w.get_platform_color(),
            w.get_platform_draw_dir()
        )
        m.refresh()
