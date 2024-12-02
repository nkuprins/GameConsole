import asyncio
from games.cubes_game.view import View
from games.cubes_game.world import World
from properties.constants import CUBES_TRIGGER_ANGLE, WIDTH, HEIGHT
from properties.state import State

class Game:

    def __init__(self, matrix):
        self._world = World()
        self._view = View(self._world, matrix)

    async def run(self):
        cubes = self._world.get_cubes() # Cache for speed
        hc = self._view.has_cube

        while self._world.is_running():
            z, y = State.orientation
            x_speed = -1 if z > CUBES_TRIGGER_ANGLE else 1 if z < -CUBES_TRIGGER_ANGLE else 0
            y_speed = -1 if y > CUBES_TRIGGER_ANGLE else 1 if y < -CUBES_TRIGGER_ANGLE else 0

            if x_speed == 0 and y_speed == 0:
                # Signal the other task to run and wait for some time
                await asyncio.sleep(0.0)
                continue

            for cube in cubes:
                new_x_speed = cube.try_accelerate(z, x_speed)
                new_y_speed = cube.try_accelerate(y, y_speed)
                new_x = min(max(cube.get_x() + new_x_speed, 0), WIDTH - 1)
                new_y = min(max(cube.get_y() + new_y_speed, 0), HEIGHT - 1)
                if hc(new_x, new_y):
                    continue
#                     if x_speed != 0 and not hc(new_x, new_y - 1):
#                         new_y -= 1
#                     elif x_speed != 0 and not hc(new_x, new_y + 1):
#                         new_y += 1
#                     if y_speed != 0 and not hc(new_x - 1, new_y):
#                         new_x -= 1
#                     elif y_speed != 0 and not hc(new_x + 1, new_y):
#                         new_x += 1
#                     else:
#                         continue

                old_x = cube.get_x()
                old_y = cube.get_y()
                cube.move(new_x, new_y)
                self._view.draw_cube(new_x, new_y, old_x, old_y, cube.get_color())
            self._view.refresh_cubes()

            # Signal the other task to run and wait for some time
            await asyncio.sleep(0.0)
