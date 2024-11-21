from ponggame.world import World
from ponggame.view import View
from consoleparts.state import State
import asyncio

# Class to run the pong game
class Game:

    def __init__(self, matrix):
    	self._world = World()
        self._view = View(self._world, matrix)

    async def run(self):
        while self._world.is_running():

            # Save old positions
            old_platform = self._world.get_platform().get_pos()
            old_ball = self._world.get_ball().get_pos()

            # Move the platform
            self._world.get_platform().move(State.direction)
            # Clear the direction
            State.direction = None
            # Move the ball
            self._world.get_ball().move()

            # Draw new game data
            self._view.draw_game(old_platform, old_ball)

            # Signal the other task to run and wait for some time
            await asyncio.sleep(0.07)

    	
