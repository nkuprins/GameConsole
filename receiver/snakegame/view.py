from snakegame.world import World
from utility import Color, WIDTH, HEIGHT, BORDER_SIZE, SCALE

class View:

    def __init__(self, world, matrix):
    	self._world = world
        self._matrix = matrix
        self._draw_init()

    def _draw_init(self):
        # Draw background
        self._matrix.draw_with_scale((0,0), Color.DARK_GREEN)
        # Draw border
        self._draw_border()
        # Draw snake head
        self._matrix.draw_with_scale(self._world.get_snake().get_pos(), Color.BLACK)

    def _draw_border(self):
        color = Color.RED
        self._matrix.draw_horizontal_line(0, color)
        self._matrix.draw_horizontal_line(HEIGHT - BORDER_SIZE, color)
        self._matrix.draw_vertical_line(0, color)
        self._matrix.draw_vertical_line(WIDTH - BORDER_SIZE, color)

    def draw_game(self, old_tail_pos):
        # Draw snake head
        self._matrix.draw_with_scale(self._world.get_snake().get_pos(), Color.BLACK)
        # Draw snake tail
        new_tail_pos = self._world.get_snake().get_body()[-1]
        self._matrix.draw_with_scale(old_tail_pos, Color.DARK_GREEN, new_tail_pos, Color.BLACK)
        # Draw food
        self._matrix.draw_with_scale(self._world.get_food().get_pos(), Color.RED)