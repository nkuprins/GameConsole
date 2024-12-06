import random
from games.cubes_game.cube import Cube
from games.parent.world_parent import WorldParent
from properties.color import Color
from properties.constants import CENTRE_X, CENTRE_Y, CUBES_GAME_SIZE, CUBES_TRIGGER_Y

class World(WorldParent):
    def __init__(self):
        super().__init__(Color.BLACK)

        # Initializes 2 maps for the acceleration functionality
        self._setup_acceleration()

        # Generate all cubes
        self._cubes = []
        for i in range(CENTRE_X - CUBES_GAME_SIZE, CENTRE_X + CUBES_GAME_SIZE):
            for j in range(CENTRE_Y - CUBES_GAME_SIZE, CENTRE_Y + CUBES_GAME_SIZE):
                color = Color.random_color()
                self._cubes.append(Cube(i, j, color, self))

    def _setup_acceleration(self):
        accelerate_map = {} # contains 5 booleans for orientation(z,y) values
        for orientation_axis in range(CUBES_TRIGGER_Y, 92):
            accelerate_map[orientation_axis] = [self._random_accelerate(orientation_axis) for _ in range(5)]
        self._accelerate_map = accelerate_map

        index_map = {} # contains index for accelerate_map for orientation(z,y) values
        for orientation_axis in range(CUBES_TRIGGER_Y, 92):
            index_map[orientation_axis] = 0
        self._index_map = index_map

    # Returns True with some probability
    # This probability depends on orientation_axis: z or y,
    # the higher the value is, the higher probability
    def _random_accelerate(self, orientation_axis):
        probability = min(max(0.006 * abs(orientation_axis), 0), 1)
        return (random.randint(0, 100) / 100) < probability

    # Returns True if speed should be doubled
    def should_accelerate(self, orientation_axis):
        orientation_axis = abs(orientation_axis)
        # Get index for random booleans array
        index = self._index_map[orientation_axis]
        # Update the index
        self._index_map[orientation_axis] = (index + 1) % 5
        # Get the random value for the index
        return self._accelerate_map[orientation_axis][index]

    def get_cubes(self):
        return self._cubes
