from gameconsole.state import State, Phase, GameOption
import snakegame.game as snakegame
import asyncio

# Class to represent game console
class Console:

    def __init__(self, matrix):
        self._matrix = matrix

    # The core of all console functionality 
    async def run(self):
        await self._show_logo()

        while True:
            if State.phase == Phase.MENU:
                await self._choose_game()
            elif State.phase == Phase.GAME:
                await self._play_game()

            # Signal the other task to run with 0
            await asyncio.sleep(0.0)

    # TODO
    async def _show_logo(self):
        # await asyncio.sleep(1.0)
        return

    # TODO
    async def _choose_game(self):
        State.phase = Phase.GAME
        State.game = GameOption.SNAKE
        return

    # TODO
    async def _play_game(self):
        if State.game == GameOption.SNAKE:
            await snakegame.Game(self._matrix).run()
        elif State.game == GameOption.PONG
