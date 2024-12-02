import games.cubes_game.game as cg
import games.pong_game.game as pg
import games.snake_game.game as sg
from games.game_over.game_over import GameOver
from properties.state import State, Phase, GameOption

class Console:

    def __init__(self, matrix):
        self._matrix = matrix

    async def run(self):
        await self._show_logo()
        game_over = GameOver(self._matrix)

        while True:
            if State.phase == Phase.MENU:
                await self._choose_game()
                State.phase = Phase.GAME_RUNNING
            elif State.phase == Phase.GAME_RUNNING:
                await self._play_game()
                State.phase = Phase.GAME_OVER
            elif State.phase == Phase.GAME_RUNNING:
                await game_over.run()
                State.phase = game_over.next_phase()

    # TODO
    async def _show_logo(self):
        # await asyncio.sleep(1.0)
        return

    # TODO
    async def _choose_game(self):
        State.game = GameOption.CUBES
        return

    # TODO
    async def _play_game(self):
        game = None
        if State.game == GameOption.SNAKE:
            game = sg.Game(self._matrix)
        elif State.game == GameOption.PONG:
            game = pg.Game(self._matrix)
        elif State.game == GameOption.CUBES:
            game = cg.Game(self._matrix)
        await game.run()