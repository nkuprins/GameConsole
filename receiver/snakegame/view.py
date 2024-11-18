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
        self._draw_border()
        # Draw snake head
        self._matrix.draw_with_scale(self._world.get_snake().get_pos(), Color.DARK_GREEN)
        # Draw food
        self._matrix.draw_with_scale(self._world.get_food().get_pos(), Color.RED)

    def _draw_border(self):
        color = Color.RED
        self._matrix.draw_horizontal_line(0, color)
        self._matrix.draw_horizontal_line(HEIGHT - BORDER_SIZE, color)
        self._matrix.draw_vertical_line(0, color)
        self._matrix.draw_vertical_line(WIDTH - BORDER_SIZE, color)

    def draw_game(self, old_head_pos, old_food_pos, old_tail_pos = None):
        return
        # Draw food
        self._matrix.draw_with_scale(self._world.get_food().get_pos(), Color.RED, old_food_pos, Color.BLACK)

        # Draw snake head
        self._matrix.draw_with_scale(self._world.get_snake().get_pos(), Color.DARK_GREEN, old_head_pos, Color.BLACK)

        if old_tail_pos is not None:
            print(old_tail_pos)
            # Draw snake tail
            new_tail_pos = self._world.get_snake().get_body()[-1]
            print(new_tail_pos)
            print("AAAAAAAAAAA")
            self._matrix.draw_with_scale(new_tail_pos, Color.DARK_GREEN, old_tail_pos, Color.BLACK)
            print("BBBBB")
