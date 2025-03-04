import asyncio
import time
from games.pong_game.view import View
from games.pong_game.world import World
from games.parent.game_parent import GameParent
from properties.direction import Direction
from properties.constants import PONG_GAME_DELAY, PONG_PLATFORM_DELAY

class Game(GameParent):

    def __init__(self, matrix):
        world = World()
        view = View(world, matrix)
        super().__init__(world, view)

    async def run(self):
        start_time = time.monotonic()
        direction = None
        while self._world.is_running():

            # Save old positions
            old_platform = self._world.get_platform().get_pos()
            old_ball = self._world.get_ball().get_pos()

            elapsed_time = time.monotonic() - start_time
            new_direction = Direction.from_orientation()
            # Move only if time elapsed or if move is in the opposite direction
            if Direction.is_opposite(direction, new_direction) or elapsed_time > PONG_PLATFORM_DELAY:
                # Move the platform
                direction = new_direction
                # print(direction)
                self._world.get_platform().move(direction)
                start_time = time.monotonic()

            # Move the ball
            self._world.get_ball().move()

            # Draw new game data
            self._view.draw_game(old_platform, old_ball)

            # Yield other task and wait
            await asyncio.sleep(max(PONG_GAME_DELAY - (self._world.get_score() * 3) / 100, 0.05))


