from games.cubes_game.cube import Cube
from games.parent.world_object import WorldObject
from properties.constants import WIDTH, HEIGHT, WORLD_SIZE, CUBES_SIZE
from properties.color import Color

# State of the cube game
class World(WorldObject):

    def __init__(self):
        super().__init__(Color.BLACK)
        self._cubes = []
        centre_x = int(WIDTH / 2)
        centre_y = int(HEIGHT / 2)
        for i in range(centre_x - CUBES_SIZE, centre_x + CUBES_SIZE):
            for j in range(centre_y - CUBES_SIZE, centre_y + CUBES_SIZE):
                color = Color.random_color()
                self._cubes.append(Cube(i, j, color, self))

    def get_cubes(self):
        return self._cubes
