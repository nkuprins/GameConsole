from game.gameobject import GameObject
from utility import SCALE, WIDTH, HEIGHT

# Class that represents a ball
class Ball:

    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self._x_speed = 1
        self._y_speed = -1

    def move(self):
        self._x += (1 + SCALE) * self._x_speed
        self._y += (1 + SCALE) * self._y_speed

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
        return x >= (WIDTH - 1 - (1 + SCALE) * 2)

    def _is_collided_with_bottom(self, x):
        return x <= (SCALE + 1)

    def _is_collided_with_side(self, y):
        return y >= (HEIGHT - 1 - (SCALE + 1) * 2) or y <= (SCALE + 1)

    def _is_collided_with_platform(self, x, y):
        platform_pos = self._world.get_platform().get_pos()
        return self._is_collided((x, y), platform_pos)
