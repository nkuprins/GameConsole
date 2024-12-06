from games.parent.view_border import ViewBorder
from properties.constants import (SNAKE_HEAD_COLOR, SNAKE_BODY_COLOR,
                                  SNAKE_FOOD_COLOR, SNAKE_BORDER_COLOR,
                                  SNAKE_BACKGROUND_COLOR)

class View(ViewBorder):

    def __init__(self, world, matrix):
        super().__init__(world, matrix, SNAKE_BACKGROUND_COLOR, SNAKE_BORDER_COLOR)
        # Draw snake head
        matrix.draw_square(world.get_snake().get_head(), SNAKE_HEAD_COLOR)
        # Draw food
        matrix.draw_square(world.get_food().get_pos(), SNAKE_FOOD_COLOR)
        matrix.refresh()

    def draw_game(self, old_head, old_food, old_tail):
        w = self._world
        m = self._matrix

        # Clear food
        self._clear_sq_at_pos(old_food)
        # Draw food
        m.draw_square(w.get_food().get_pos(), SNAKE_FOOD_COLOR)

        # Clear snake head
        self._clear_sq_at_pos(old_head)
        # Draw snake head
        m.draw_square(w.get_snake().get_head(), SNAKE_HEAD_COLOR)

        if old_tail is not None:
            # Clean tail
            self._clear_sq_at_pos(old_tail)
        # Draw snake body
        self._draw_body()
        m.refresh()

    def _draw_body(self):
        body = self._world.get_snake().get_body()
        for body_part in body:
            self._matrix.draw_square(body_part, SNAKE_BODY_COLOR)
