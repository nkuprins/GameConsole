
from utility import Direction, BORDER_SIZE, WIDTH, HEIGHT, SCALE, to_coord
from snakegame.food import Food

class Snake:

    # (x, y) is a point that should be at the top-left corner of a snake
    # Note, at the start of the game, if the world scale is set to 0,
    # this is the only point of the snake
    def __init__(self, x, y, world):
        self._direction_coord = to_coord(Direction.RIGHT)
        self._x = x
        self._y = y
        self._world = world
        self._body = []

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_pos(self):
        return (self._x, self._y)

    def get_body(self):
        return self._body

    def set_direction(self, new_direction):
        self._direction = to_coord(new_direction)

    def move(self):
        new_x = self._x + self._direction_coord[0]
        new_y = self._y + self._direction_coord[1]

        if self._is_collided_with_body(new_x, new_y) or self._is_collided_with_border(new_x, new_y):
            self._world.end_game()
            return

        if self._is_collided_with_food(new_x, new_y):
            self._body.append((0,0))
            self._world.get_food().move()
            self._world.increase_score()

        self._update_body()
        self._x = new_x
        self._y = new_y

    def _update_body(self):
        # All elements from len(body) - 1...1 move to the place of the next one.
        for i in range(len(self._body) - 1, 0, -1):
            self.body[i] = (self._body[i - 1][0], self._body[i - 1][1]);

        # The first body element after snake's head is at index 0. It moves to old snake's head position.
        if (len(self._body) != 0):
            self._body[0] = (self._x, self._y)

    def _is_collided_with_border(self, x, y):
        return x <= BORDER_SIZE or y <= BORDER_SIZE or \
            x >= WIDTH - BORDER_SIZE or y >= HEIGHT - BORDER_SIZE

    def _is_collided_with_body(self, x, y):
        for body_part in self._body:
            if body_part[0] == x and body_part[1] == y:
                return True
        return False

    def is_collided_with_snake(self, x, y):
        return self._is_collided_with_body(x, y) or self._x == x and self._y == y

    def _is_collided_with_food(self, x, y):
        food = self._world.get_food()
        food_x_end = food.get_x() + SCALE
        food_y_end = food.get_y() + SCALE

        for i in range(x, x + 1 + SCALE):
            for j in range(y, y + 1 + SCALE):
                if (i >= food.get_x() and i <= food_x_end) and \
                    (j >= food.get_y() and j <= food_y_end):
                    return True

        return False
