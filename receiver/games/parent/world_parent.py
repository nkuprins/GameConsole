# State for running games
class WorldParent:

    def __init__(self, background_color):
        self._running = True
        self._lost = False
        self._score = 0
        self._background_color = background_color

    def is_running(self):
        return self._running

    def end_game(self, has_lost):
        self._running = False
        self._lost = has_lost

    def has_lost(self):
        return self._lost

    def get_score(self):
        return self._score

    def increase_score(self):
        self._score += 1

    def get_background_color(self):
        return self._background_color
