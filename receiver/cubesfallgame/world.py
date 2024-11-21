from cubesfallgame.cube import Cube

from utility import WIDTH, HEIGHT, SCALE, CUBES_SIZE, Color

# State of the pong game
class World:

    def __init__(self):
        self._running = True
        self._cubes = []
        centre_x = int(WIDTH / 2)
        centre_y = int(HEIGHT / 2)
        for i in range(centre_x - CUBES_SIZE, centre_x + CUBES_SIZE):
            for j in range(centre_y - CUBES_SIZE, centre_y + CUBES_SIZE):
                color = Color.random_color()
                self._cubes.append(Cube(i, j, color, self))

    def get_cubes(self):
        return self._cubes

    def is_running(self):
        return self._running

    def end_game(self):
        self._running = False
