from games.parent.view_border import ViewBorder
from properties.constants import PONG_PLATFORM_COLOR, PONG_BALL_COLOR, PONG_PLATFORM_SIZE
from properties.direction import Direction

class View(ViewBorder):

    def __init__(self, world, matrix):
        super().__init__(world, matrix)
        # Draw platform
        matrix.draw_rectangle(
            world.get_platform().get_pos(),
            PONG_PLATFORM_SIZE,
            PONG_PLATFORM_COLOR,
            Direction.DOWN
        )
        # Draw ball
        matrix.draw_square(world.get_ball().get_pos(), PONG_BALL_COLOR)
        matrix.refresh()

    def draw_game(self, old_platform, old_ball):
        w = self._world
        m = self._matrix

        # Clear ball
        self._clear_sq_at_pos(old_ball)
        # Draw ball
        m.draw_square(w.get_ball().get_pos(), PONG_BALL_COLOR)

        # Clear platform
        self._clear_rct_at_pos(old_platform, w.get_platform_draw_size(), w.get_platform_draw_dir())
        # Draw platform
        m.draw_rectangle(
            w.get_platform().get_pos(),
            PONG_PLATFORM_SIZE,
            PONG_PLATFORM_COLOR,
            Direction.DOWN
        )
        m.refresh()
