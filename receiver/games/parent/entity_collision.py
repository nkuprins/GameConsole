from games.parent.entity_parent import EntityParent
from properties.constants import WORLD_SIZE, WIDTH, HEIGHT

# Entity with collision functions
class EntityCollision(EntityParent):

    def __init__(self, x, y, world):
        super().__init__(x, y, world)

    # True if pos1 is collided with pos2
    def _is_collided_with_pos(self, pos1, pos2):
        x_start1, y_start1 = pos1
        x_end1 = x_start1 + WORLD_SIZE
        y_end1 = y_start1 + WORLD_SIZE

        x_start2, y_start2 = pos2
        x_end2 = x_start2 + WORLD_SIZE
        y_end2 = y_start2 + WORLD_SIZE

        return x_end1 >= x_start2 and x_start1 <= x_end2 and \
            y_end1 >= y_start2 and y_start1 <= y_end2

    def _is_collided_with_range(self, start, end, coord):
        return start >= coord and coord <= end

    # Top from a vertical position
    def _is_collided_with_top_v(self, x):
        return x >= (WIDTH - 1 - WORLD_SIZE)

    # Top from a horizontal position
    def _is_collided_with_top_h(self, y):
        return y <= WORLD_SIZE

    # Bottom from a vertical position
    def _is_collided_with_bottom_v(self, x):
        return x <= WORLD_SIZE

    # Bottom from a horizontal position
    def _is_collided_with_bottom_h(self, y):
        return y >= (HEIGHT - 1 - WORLD_SIZE)

    # Side from a vertical position
    def _is_collided_with_side_v(self, y):
        return self._is_collided_with_top_h(y) or self._is_collided_with_bottom_h(y)

    # Side from a horizontal position
    def _is_collided_with_side_h(self, x):
        return self._is_collided_with_top_v(x) or self._is_collided_with_bottom_v(x)

    def _is_collided_with_border(self, x, y):
        return self._is_collided_with_top_h(y) or self._is_collided_with_bottom_h(y) or \
            self._is_collided_with_side_h(x)
