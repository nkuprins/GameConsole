from games.cubes_game.cube import Cube
from games.parent.world_object import WorldObject
from properties.constants import WIDTH, HEIGHT, WORLD_SIZE, CUBES_GAME_SIZE, CUBES_GAME_TRIGGER
from properties.color import Color
import random

# State of the cube game
class World(WorldObject):

    def __init__(self):
        super().__init__(Color.BLACK)

        # Generate random value beforehand for efficiency
        self._generate_accelerations()

        self._cubes = []
        centre_x = int(WIDTH / 2)
        centre_y = int(HEIGHT / 2)
        for i in range(centre_x - CUBES_GAME_SIZE, centre_x + CUBES_GAME_SIZE):
            for j in range(centre_y - CUBES_GAME_SIZE, centre_y + CUBES_GAME_SIZE):
                color = Color.random_color()
                self._cubes.append(Cube(i, j, color, self))

    def _generate_accelerations():
        accelerate_map = {}
        for orientation_axis in range(CUBES_GAME_TRIGGER, 102):
            for _ in range(5):
                accelerate_map[orientation_axis] = self._random_speed(orientation_axis)
        self._accelerate_map = accelerate_map

        index_map = {}
        for orientation_axis in range(CUBES_GAME_TRIGGER, 102):
            index_map[orientation_axis] = 0
        self._index_map = index_map

    def _random_accelerate(self, orientation_axis):
        probability = min(max(0.006 * abs(orientation_axis), 0), 1)
        return (random.randint(0, 100) / 100) < probability

    def should_accelerate(self, orientation_axis):
        orientation_axis = abs(orientation_axis)
        index = self._index_map[orientation_axis]
        result = self._accelerate_map[orientation_axis][index]
        self._index_map[orientation_axis] = (index + 1) % 5
        return result

    def get_cubes(self):
        return self._cubes
