from games.parent.entity_collision import EntityCollision
from properties.direction import Direction


class Snake(EntityCollision):

    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self._direction = Direction.RIGHT
        self._body = []

    def get_head(self):
        return self.get_pos()

    def get_tail(self):
        if len(self._body) > 0:
            return self._body[-1]
        return None

    def get_body(self):
        return self._body

    def set_direction(self, new_direction):
        # Return if we try to set the opposite direction
        # e.g. if we are UP we can not immediately go DOWN
        if new_direction is None or Direction.is_opposite(new_direction, self._direction):
            return

        self._direction = new_direction

    def move(self):
        x_speed, y_speed = Direction.to_speed(self._direction)
        new_x = self._x + x_speed
        new_y = self._y + y_speed

        if self._is_collided_with_body(new_x, new_y) or self._is_collided_with_border(new_x, new_y):
            self._world.end_game(True)
            return

        if self._is_collided_with_food(new_x, new_y):
            self._body.append((0, 0))
            self._world.get_food().random_spawn()
            self._world.increase_score()

        self._move_body()
        self._x = new_x
        self._y = new_y

    def _move_body(self):
        # All elements from len(body)-1...1 move to the place of the next one
        for i in range(len(self._body) - 1, 0, -1):
            self._body[i] = (self._body[i - 1][0], self._body[i - 1][1])

        # The first body element after snake head is at index 0
        # Move it to old snake's head position
        if len(self._body) != 0:
            self._body[0] = (self._x, self._y)

    def _is_collided_with_body(self, x, y):
        for body_part in self._body:
            if self._is_collided_with_pos((x, y), body_part):
                return True
        return False

    def is_collided_with_snake(self, x, y):
        return self._is_collided_with_body(x, y) or self._is_collided_with_pos((x, y), self.get_head())

    def _is_collided_with_food(self, x, y):
        food_pos = self._world.get_food().get_pos()
        return self._is_collided_with_pos((x, y), food_pos)
