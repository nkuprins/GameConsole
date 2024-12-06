import asyncio
import time
from games.cubes_game.view import View
from games.cubes_game.world import World
from games.parent.game_parent import GameParent
from properties.constants import CUBES_TRIGGER_Z, CUBES_TRIGGER_Y, CUBES_TIMEOUT, WIDTH, HEIGHT
from properties.state import State

# This game may have slightly different structure of the code
# but this was done to maximize the efficiency of the program
class Game(GameParent):

    def __init__(self, matrix):
        world = World()
        view = View(world, matrix)
        super().__init__(world, view)
        self._cubes = self._world.get_cubes() # to cache

    async def run(self):
        # Timer to exit game
        start_time = time.monotonic()
        # Every millisecond matters, so we reset time on bool
        reset_time = False

        while self._world.is_running():
            z, y = State.orientation
            # Determine speed based on orientation
            x_speed = -1 if z > CUBES_TRIGGER_Z else 1 if z < -CUBES_TRIGGER_Z else 0
            y_speed = -1 if y > CUBES_TRIGGER_Y else 1 if y < -CUBES_TRIGGER_Y else 0

            # If no speed, then check for timeout
            if x_speed == 0 and y_speed == 0:
                if reset_time:
                    start_time = time.monotonic()
                    reset_time = False

                elapsed_time = time.monotonic() - start_time
                if elapsed_time > CUBES_TIMEOUT:
                    self._world.end_game(False)
                    return

                await asyncio.sleep(0.0) # yield other task
                continue

            reset_time = True
            self._process_cubes(z, y, x_speed, y_speed)

            await asyncio.sleep(0.0) # yield other task

    def _process_cubes(self, z, y, x_speed, y_speed):
        for cube in self._cubes:
            new_x_speed = cube.try_accelerate(z, x_speed)
            new_y_speed = cube.try_accelerate(y, y_speed)
            new_x = min(max(cube.get_x() + new_x_speed, 0), WIDTH - 1)
            new_y = min(max(cube.get_y() + new_y_speed, 0), HEIGHT - 1)
            # Skip if position is taken
            if self._view.has_cube(new_x, new_y):
                continue

            old_x = cube.get_x()
            old_y = cube.get_y()
            cube.move(new_x, new_y)
            self._view.draw_cube(new_x, new_y, old_x, old_y, cube.get_color())
        self._view.refresh_cubes()
