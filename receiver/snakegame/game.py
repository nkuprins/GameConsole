from snakegame.world import World
from snakegame.view import View
from state import State

class Game:
    
    def __init__(self, matrix):
    	self._world = World()
        self._view = View(self._world, self._matrix)

    def run(self):
        while self._world.is_running():
            self._world.get_snake().set_direction(State.DIRECTION)
            old_body = self._world.get_snake().get_body()
            self._world.get_snake().move()
            self._view.draw_game(old_body[-1])
            await asyncio.sleep(1.0)

    	
