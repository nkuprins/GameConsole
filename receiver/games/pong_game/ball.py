from games.parent.entity_collision import EntityCollision
from properties.constants import WORLD_SIZE, PONG_PLATFORM_SIZE

class Ball(EntityCollision):

    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self._x_speed = 1 + WORLD_SIZE
        self._y_speed = 1 + WORLD_SIZE

    def move(self):
        new_x = self._get_x_movement()
        new_y = self._get_y_movement()

        if self._is_collided_with_side_v(new_y):
            self._y_speed *= -1
            new_y = self._get_y_movement()
        elif self._is_collided_with_platform(new_x, new_y):
            self._x_speed *= -1
            new_x = self._get_x_movement()
            self._world.increase_score()
        elif self._is_collided_with_top_v(new_x):
            self._x_speed *= -1
            new_x = self._get_x_movement()
        elif self._is_collided_with_bottom_v(new_x):
            self._world.end_game(True)
            return

        self._x = new_x
        self._y = new_y

    def _get_x_movement(self):
        return self._x + self._x_speed

    def _get_y_movement(self):
        return self._y + self._y_speed

    def _is_collided_with_platform(self, x, y):
        platform_x, platform_y = self._world.get_platform().get_pos()

        for i in range(PONG_PLATFORM_SIZE):
            new_pos = (platform_x, platform_y + i * (WORLD_SIZE + 1))
            if self._is_collided_with_pos((x, y), new_pos):
                return True
        return False

