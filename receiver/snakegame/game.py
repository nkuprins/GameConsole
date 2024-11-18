from snakegame.world import World
from snakegame.view import View
from gameconsole.state import State
import asyncio

class Game:

    def __init__(self, matrix):
    	self._world = World()
        self._view = View(self._world, matrix)

    async def run(self):
        while self._world.is_running():
            self._world.get_snake().set_direction(State.DIRECTION)

            old_head_pos = self._world.get_snake().get_pos()
            old_food_pos = self._world.get_food().get_pos()
            body = self._world.get_snake().get_body()

            old_tail_pos = None
            if len(body) > 0:
                old_tail_pos = body[-1]

            self._world.get_snake().move()

            if old_tail_pos is not None:
                self._view.draw_game(old_head_pos, old_food_pos, old_tail_pos)
            else:
                self._view.draw_game(old_head_pos, old_food_pos)

            await asyncio.sleep(2.0)

    	
