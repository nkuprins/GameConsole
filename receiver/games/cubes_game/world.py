import random

from games.cubes_game.cube import Cube
from games.parent.world_parent import WorldParent
from properties.color import Color
from properties.constants import WIDTH, HEIGHT, CUBES_GAME_SIZE, CUBES_TRIGGER_ANGLE


class World(WorldParent):

    def __init__(self):
        super().__init__(Color.BLACK)

        # Generate random value beforehand for efficiency
        self._generate_accelerations()

        self._cubes = []
        centre_x = int(WIDTH / 2)
        centre_y = int(HEIGHT / 2)
        # Generate all cubes
        for i in range(centre_x - CUBES_GAME_SIZE, centre_x + CUBES_GAME_SIZE):
            for j in range(centre_y - CUBES_GAME_SIZE, centre_y + CUBES_GAME_SIZE):
                color = Color.random_color()
                self._cubes.append(Cube(i, j, color, self))

    # TODO comment
    def _generate_accelerations(self):
        accelerate_map = {}
        for orientation_axis in range(CUBES_TRIGGER_ANGLE, 92):
            accelerate_map[orientation_axis] = [self._random_accelerate(orientation_axis) for _ in range(5)]
        self._accelerate_map = accelerate_map

        index_map = {}
        for orientation_axis in range(CUBES_TRIGGER_ANGLE, 92):
            index_map[orientation_axis] = 0
        self._index_map = index_map

    # TODO comment
    def _random_accelerate(self, orientation_axis):
        probability = min(max(0.006 * abs(orientation_axis), 0), 1)
        return (random.randint(0, 100) / 100) < probability

    # TODO comment
    def should_accelerate(self, orientation_axis):
        orientation_axis = abs(orientation_axis)
        index = self._index_map[orientation_axis]
        self._index_map[orientation_axis] = (index + 1) % 5
        return self._accelerate_map[orientation_axis][index]

    def get_cubes(self):
        return self._cubes
