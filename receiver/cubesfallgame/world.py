from cubesfallgame.cube import Cube

from utility import WIDTH, HEIGHT, SCALE, CUBES_SIZE, Color

# State of the pong game
class World:

    def __init__(self):
        self._cubes = []
        centre_x = WIDTH / 2 
        centre_y = HEIGHT / 2
        for i in range(centre_x - CUBES_SIZE, centre_x + CUBES_SIZE + 1):
            for j in range(centre_y - CUBES_SIZE, centre_y + CUBES_SIZE + 1):
                color = Color.RED # TODO RANDOM GENERATION
                cubes.append(Cube(i, j, color, self))

    def get_cubes(self):
        return self._platform

    def is_running(self):
        return self._running

    def end_game(self):
        self._running = False
