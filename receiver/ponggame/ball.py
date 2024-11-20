from utility import SCALE, WIDTH

# Class that represents a ball
class Ball:

    # (x, y) is the anchor point
    def __init__(self, x, y, world):
        self._x = x
        self._y = y
        self._x_speed = -1
        self._y_speed = 1
        self._world = world

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_pos(self):
        return (self._x, self._y)

    def move(self):
        new_x += (1 + SCALE) * self._x_speed
        new_y += (1 + SCALE) * self._y_speed

        if self._is_collided_with_side(new_x):
            self._x_speed *= -1
        elif self._is_collided_with_platform(new_x, new_y):
            self._ball_x_speed = self._ball_x_speed * -1 + 1 
            self._world.increase_score()
        elif self._is_collided_with_top(new_y):
            self._y_speed *= -1
        elif self._is_collided_with_bottom(new_y):
            self._world.end_game()

        self._x = new_x
        self._y = new_y

    def _is_collided_with_side(self, x):
        return x >= (self._world.get_width() - 1 - SCALE) or x <= SCALE

    def _is_collided_with_top(self, y):
        return y >= (self._world.get_height() - 1 - SCALE)

    def _is_collided_with_bottom(self, y):
        return y <= 0

    def _is_collided_with_platform(self, x, y):
        platform_pos = self._world.get_platform().get_pos()
        return self._is_collided((x, y), platform_pos)

    # True if pos_a is collided with pos_b
    def _is_collided(self, pos_a, pos_b):
        a_start_x = pos_a[0]
        a_start_y = pos_a[1]
        a_end_x = pos_a[0] + SCALE
        a_end_y = pos_a[1] + SCALE
        b_start_x = pos_b[0]
        b_start_y = pos_b[1]
        b_end_x = pos_b[0] + SCALE
        b_end_y = pos_b[1] + SCALE

        return a_end_x >= b_start_x and a_start_x <= b_end_x and \
                a_end_y >= b_start_y and a_start_y <= b_end_y