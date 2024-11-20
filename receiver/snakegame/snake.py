
from utility import Direction, WIDTH, HEIGHT, SCALE
from snakegame.food import Food

# Class that represents a snake
class Snake:

    # (x, y) is the anchor point
    def __init__(self, x, y, world):
        self._direction = Direction.RIGHT
        self._x = x
        self._y = y
        self._world = world
        self._body = []

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_head(self):
        return (self._x, self._y)

    def try_get_tail(self):
        if len(self._body) > 0:
            return self._body[-1]
        return None

    def get_body(self):
        return self._body

    def set_direction(self, new_direction):
        if new_direction is None: return

        # Return if we try to set the opposite direction (if we are UP we can not immediately go DOWN)
        if new_direction == Direction.RIGHT and self._direction == Direction.LEFT or \
            new_direction == Direction.LEFT and self._direction == Direction.RIGHT or \
            new_direction == Direction.UP and self._direction == Direction.DOWN or \
            new_direction == Direction.DOWN and self._direction == Direction.UP:
                return

        self._direction = new_direction

    def move(self):
        new_x = self._x + Direction.to_coord(self._direction)[0]
        new_y = self._y + Direction.to_coord(self._direction)[1]

        if self._is_collided_with_body(new_x, new_y) or self._is_collided_with_border(new_x, new_y):
            self._world.end_game()
            return

        if self._is_collided_with_food(new_x, new_y):
            self._body.append((0,0))
            self._world.get_food().random_spawn()
            self._world.increase_score()

        self._move_body()
        self._x = new_x
        self._y = new_y

    def _move_body(self):
        # All elements from len(body)-1...1 move to the place of the next one.
        for i in range(len(self._body) - 1, 0, -1):
            self._body[i] = (self._body[i - 1][0], self._body[i - 1][1]);

        # The first body element after snake's head is at index 0. It moves to old snake's head position.
        if (len(self._body) != 0):
            self._body[0] = (self._x, self._y)

    # if scale is 0 then border is at pixel 0, and if 1 then at 0-1 pixels
    def _is_collided_with_border(self, x, y):
        return x <= SCALE or y <= SCALE or \
            x >= (WIDTH - 1 - SCALE) or y >= (HEIGHT - 1 - SCALE)
    
    def _is_collided_with_body(self, x, y):
        for body_part in self._body:
            if (self._is_collided((x, y), body_part)):
                return True
        return False

    def is_collided_with_snake(self, x, y):
        return self._is_collided_with_body(x, y) or self._x == x and self._y == y

    def _is_collided_with_food(self, x, y):
        food_pos = self._world.get_food().get_pos()
        return self._is_collided((x, y), food_pos)

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