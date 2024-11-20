from snakegame.world import World
from utility import Color, WIDTH, HEIGHT, BORDER_SIZE, SCALE

class View:

    def __init__(self, world, matrix):
    	self._world = world
        self._matrix = matrix
        self._draw_init()

    def _draw_init(self):
        # Draw background
        self._matrix.draw_background(Color.BLACK)
        # Draw border
        self._matrix.draw_border(Color.RED)
        # Draw snake head
        self._matrix.draw_with_scale(self._world.get_snake().get_pos(), Color.DARK_GREEN)
        # Draw food
        self._matrix.draw_with_scale(self._world.get_food().get_pos(), Color.RED)

    def _draw_body(self):
        body = self._world.get_snake().get_body()
        for body_part in body:
            self._matrix.draw_with_scale(body_part, Color.DARK_GREEN)

    def draw_game(self, old_head, old_food, old_tail):
        # Draw food
        self._matrix.draw_with_scale(self._world.get_food().get_pos(), Color.RED, old_food, Color.BLACK)

        # Draw snake head
        self._matrix.draw_with_scale(self._world.get_snake().get_pos(), Color.DARK_GREEN, old_head, Color.BLACK)

        # Clean tail
        if old_tail_pos is not None:
            self._matrix.draw_with_scale(old_tail_pos, Color.BLACK)
            # Draw snake body
            self._draw_body()
