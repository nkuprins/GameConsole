from games.snake_game.snake import Snake
from games.snake_game.food import Food
from games.parent.world_border import WorldBorder
from properties.constants import HEIGHT, WORLD_SIZE
from properties.color import Color

class World(WorldBorder):

    def __init__(self):
        super().__init__(Color.BLACK, Color.ORANGE)
        self._snake = Snake(WORLD_SIZE + 3, int(HEIGHT / 2), self)
        self._food = Food(11 + WORLD_SIZE, int(HEIGHT / 2), self)

    def get_snake(self):
        return self._snake

    def get_food(self):
        return self._food