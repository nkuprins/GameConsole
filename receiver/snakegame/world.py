from snakegame.snake import Snake
from snakegame.food import Food

class World:

    def __init__(self):
        self._snake = Snake(10, height / 2, self)
        self._food = Food(width - 10, height / 2, self)

        self._running = True
        self._score = 0

    def get_snake(self):
        return self._snake

    def get_food(self):
        return self._food

    def is_running(self):
        return self._running

    def get_score(self):
        return self._score

    def end_game(self):
        self._running = False

    def increase_score(self):
        self._score = self._score + 1
