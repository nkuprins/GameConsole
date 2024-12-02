from games.parent.entity_parent import EntityParent
from properties.constants import HEIGHT, WORLD_SIZE
from properties.direction import Direction

class Platform(EntityParent):

    def __init__(self, x, y, world):
        super().__init__(x, y, world)

    def move(self, direction):
        if direction is None or \
            direction == Direction.LEFT or direction == Direction.RIGHT:
            return

        new_y = self._y + Direction.to_speed(direction)[1]
        min_y = WORLD_SIZE + 1
        max_y = HEIGHT - (WORLD_SIZE + 1) * (self._world.get_platform_draw_size() + 1)
        self._y = min(max(new_y, min_y), max_y)
