from games.cubes_game.world import World
from games.cubes_game.view import View
from properties.state import State
from properties.constants import CUBES_GAME_TRIGGER
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
            orientation = (-30, 0)
            z = orientation[0]
            y = orientation[1]
            speed_x = 1 if z > CUBES_GAME_TRIGGER else -1 if z < -CUBES_GAME_TRIGGER else 0
            speed_y = 1 if y > CUBES_GAME_TRIGGER else -1 if y < -CUBES_GAME_TRIGGER else 0

            if speed_x == 0 and speed_y == 0:
                continue

            #subtract_wait_sec = min(pow(abs(z) + abs(y), 2) / 10, 25) / 1000
            #is_diagonal_move = False

            for cube in cubes:
                new_speed_x = cube.try_accelerate(z, speed_x)
                new_speed_y = cube.try_accelerate(y, speed_y)
                new_x = min(max(cube.get_x() + new_speed_x, 0), WIDTH - 1)
                new_y = min(max(cube.get_y() + new_speed_y, 0), HEIGHT - 1)
                if self._view.has_cube(new_x, new_y):
                    continue
                old_x = cube.get_x()
                old_y = cube.get_x()
                cube.move(new_x, new_y)
                self._view.draw_cube(new_x, new_y, old_x, old_y)
                # if old_pos[0] != new_pos[0] and old_pos[1] != new_pos[1]:
                #   is_diagonal_move = True
                # if is_diagonal_move:
                #   subtract_wait_sec -= 0.20
            self._view.refresh_cubes()

            # Signal the other task to run and wait for some time
            await asyncio.sleep(0.0)

    	
