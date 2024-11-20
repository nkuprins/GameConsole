from ponggame.platform import Platform
from ponggame.ball import Ball
from utility import HEIGHT, SCALE

# State of the pong game
class World:

    def __init__(self):
        self._platform = Platform(4 + SCALE, int(HEIGHT / 2), self)
        self._ball = Ball(self._platform.get_x() + 1 + SCALE, int(HEIGHT / 2), self)

        self._running = True
        self._score = 0

    def get_platform(self):
        return self._platform

    def get_ball(self):
        return self._ball

    def is_running(self):
        return self._running

    def get_score(self):
        return self._score

    def end_game(self):
        self._running = False

    def increase_score(self):
        self._score = self._score + 1
