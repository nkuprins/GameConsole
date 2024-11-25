from games.pong_game.world import World
from games.pong_game.view import View
from properties.state import State
from properties.direction import Direction
import asyncio
import time

# Class to run the pong game
class Game:

    def __init__(self, matrix):
    	self._world = World()
        self._view = View(self._world, matrix)

    async def run(self):
        start_time = time.monotonic()
        direction = None
        while self._world.is_running():

            # Save old positions
            old_platform = self._world.get_platform().get_pos()
            old_ball = self._world.get_ball().get_pos()

            elapsed_time = time.monotonic() - start_time
            new_direction = Direction.from_orientation()
            if Direction.opposite(direction, new_direction) or elapsed_time > 0.2:
                # Move the platform
                direction = new_direction
                print(direction)
                self._world.get_platform().move(direction)
                start_time = time.monotonic()

            # Move the ball
            self._world.get_ball().move()

            # Draw new game data
            self._view.draw_game(old_platform, old_ball)

            # Signal the other task to run and wait for some time
            await asyncio.sleep(max(0.6 - self._world.get_score() / 100, 0.05))

    	
