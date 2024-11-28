from games.cubes_game.world import World
from games.cubes_game.view import View
from properties.state import State
from properties.constants import CUBES_GAME_TRIGGER, WIDTH, HEIGHT
import asyncio
import time

# Class to run the cube game
class Game:

    def __init__(self, matrix):
    	self._world = World()
        self._view = View(self._world, matrix)

    async def run(self):
        cubes = self._world.get_cubes() # Cache for speed

        while self._world.is_running():
            z, y = State.orientation
            x_speed = 1 if z > CUBES_GAME_TRIGGER else -1 if z < -CUBES_GAME_TRIGGER else 0
            y_speed = -1 if y > CUBES_GAME_TRIGGER else 1 if y < -CUBES_GAME_TRIGGER else 0

            if x_speed == 0 and y_speed == 0:
                await asyncio.sleep(0.6)
                continue

            for cube in cubes:
                new_x_speed = cube.try_accelerate(z, x_speed)
                new_y_speed = cube.try_accelerate(y, y_speed)
                new_x = min(max(cube.get_x() + new_x_speed, 0), WIDTH - 1)
                new_y = min(max(cube.get_y() + new_y_speed, 0), HEIGHT - 1)
                if self._view.has_cube(new_x, new_y):
                    continue
                old_x = cube.get_x()
                old_y = cube.get_y()
                cube.move(new_x, new_y)
                self._view.draw_cube(new_x, new_y, old_x, old_y, cube.get_color())
            self._view.refresh_cubes()

            # Signal the other task to run and wait for some time
            await asyncio.sleep(0.6)

    	
