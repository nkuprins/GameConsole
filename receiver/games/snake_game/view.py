from games.snake_game.world import World
from properties.color import Color
from games.parent.view_border import ViewBorder

class View(ViewBorder):

    def __init__(self, world, matrix):
        super().__init__(world, matrix)
        # Draw snake head
        matrix.draw_square(world.get_snake().get_head(), world.get_snake_color())
        # Draw food
        matrix.draw_square(world.get_food().get_pos(), world.get_food_color())
        matrix.refresh()

    def _draw_body(self):
        body = self._world.get_snake().get_body()
        for body_part in body:
            self._matrix.draw_square(body_part, self._world.get_snake_color())

    def draw_game(self, old_head, old_food, old_tail):
        w = self._world

        # Clear food
        self._clear_sq_at_pos(old_food)
        # Draw food
        self._matrix.draw_square(w.get_food().get_pos(), w.get_food_color())

        # Clear snake head
        self._clear_sq_at_pos(old_head)
        # Draw snake head
        self._matrix.draw_square(w.get_snake().get_head(), w.get_snake_color())

        if old_tail is not None:
            # Clean tail
            self._clear_sq_at_pos(old_tail)
        # Draw snake body
        self._draw_body()
        self._matrix.refresh()
