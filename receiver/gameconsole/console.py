from state import State, Phase, GameOption
import snakegame.game as snakegame

class Console:

    def __init__(self, matrix):
        self._matrix = matrix
        
    async def run():
        await self._show_logo()
        while True:
            match State.PHASE:
                case Phase.MENU: await self._choose_game()
                case Phase.GAME: await self._play_game()

            await asyncio.sleep(0.0)

    # TODO
    async def _show_logo():
        return

    # TODO
    async def _choose_game(direction):
        State.PHASE = PHASE.GAME
        State.GAME = GameOption.SNAKE
        return

    async def _play_game():
        match State.GAME:
            case GameOption.SNAKE: snakegame.Game(self._matrix).run()
            case _: return
