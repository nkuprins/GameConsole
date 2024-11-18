from gameconsole.state import State, Phase, GameOption
import snakegame.game as snakegame
import asyncio

class Console:

    def __init__(self, matrix):
        self._matrix = matrix

    async def run(self):
        await self._show_logo()
        while True:
            if State.PHASE == Phase.MENU:
                await self._choose_game(State.DIRECTION)
            elif State.PHASE == Phase.GAME:
                await self._play_game()

            await asyncio.sleep(0.0)

    # TODO
    async def _show_logo(self):
        return

    # TODO
    async def _choose_game(self, direction):
        State.PHASE = Phase.GAME
        State.GAME = GameOption.SNAKE
        return

    async def _play_game(self):
        if State.GAME == GameOption.SNAKE:
            await snakegame.Game(self._matrix).run()
