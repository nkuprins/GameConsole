from games.snake_game.world import World
from games.snake_game.view import View
from properties.direction import Direction
from properties.constants import SNAKE_GAME_DELAY
import asyncio

class Game:

    def __init__(self, matrix):
        self._world = World()
        self._view = View(self._world, matrix)

    async def run(self):
        while self._world.is_running():
            direction = Direction.from_orientation()
            # print(direction)
            self._world.get_snake().set_direction(direction)

            # Save old snake positions
            old_head = self._world.get_snake().get_head()
            old_food = self._world.get_food().get_pos()
            old_tail = self._world.get_snake().get_tail()

            # Move the snake
            self._world.get_snake().move()
            # Draw new game data
            self._view.draw_game(old_head, old_food, old_tail)

            # Signal the other task to run and wait for some time
            await asyncio.sleep(SNAKE_GAME_DELAY)