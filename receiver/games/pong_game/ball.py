from game.gameobject import GameObject
from properties.constants import WIDTH, HEIGHT, WORLD_SIZE


# Class that represents a ball
class Ball:

    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self._x_speed = 1
        self._y_speed = -1

    def move(self):
        self._x += (1 + WORLD_SIZE) * self._x_speed
        self._y += (1 + WORLD_SIZE) * self._y_speed

        if self._is_collided_with_side(self._y):
            self._y_speed *= -1
        elif self._is_collided_with_platform(self._x, self._y):
            self._y_speed *= -1
            self._world.increase_score()
        elif self._is_collided_with_top(self._x):
            self._x_speed *= -1
        elif self._is_collided_with_bottom(self._x):
            self._world.end_game()

    def _is_collided_with_top(self, x):
        return x >= (WIDTH - 1 - (1 + WORLD_SIZE) * 2)

    def _is_collided_with_bottom(self, x):
        return x <= (WORLD_SIZE + 1)

    def _is_collided_with_side(self, y):
        return y >= (HEIGHT - 1 - (WORLD_SIZE + 1) * 2) or y <= (WORLD_SIZE + 1)

    def _is_collided_with_platform(self, x, y):
        y_move = WORLD_SIZE + 1
        platform_pos = self._world.get_platform().get_pos()
        for i in range(self._world.get_platform_draw_size()):
            new_pos = (platform_pos[0], platform_pos[1] + i * y_move)
            if self._is_collided((x, y), new_pos):
                return True

        return False
        
