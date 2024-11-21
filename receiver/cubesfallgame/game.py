from cubesfallgame.world import World
from cubesfallgame.view import View
from gameconsole.state import State
from utility import CUBES_SENSITIVITY
import asyncio

# Class to run the pong game
class Game:

    def __init__(self, matrix):
    	self._world = World()
        self._view = View(self._world, matrix)

    async def run(self):
        while self._world.is_running():
            orientation = State.orientation
            z = orientation[0]
            y = orientation[1]
            if z == 0 && y == 0 || abs(z) < CUBES_SENSITIVITY && abs(y) < CUBES_SENSITIVITY:
                await asyncio.sleep(0.3)
                continue

            subtract_wait_sec = min(pow(abs(z) + abs(y), 2) / 10, 225) / 1000
            is_diagonal_move = False
            for cube in self._world.get_cubes():
                new_pos = cube.get_move_coord(orientation)
                if new_pos is None: 
                    break
                elif if self._view.has_cube(new_pos): 
                    continue
                old_pos = cube.get_pos()
                cube.move(new_pos)
                self._view.draw_cube(cube, old_pos)

                if old_pos[0] != new_pos[0] and old_pos[1] != new_pos[1]:
                    is_diagonal_move = True

            if is_diagonal_move:
                subtract_wait_sec -= 0.20

            # Signal the other task to run and wait for some time
            await asyncio.sleep(0.250 - subtract_wait_sec)

    	
