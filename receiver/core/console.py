import games.cubes_game.game as cg
import games.pong_game.game as pg
import games.snake_game.game as sg
from games.game_over.game_over import GameOver
from games.menu.main_menu import MainMenu
from properties.state import Phase, GameOption
from adafruit_bitmap_font import bitmap_font

class Console:

    def __init__(self, matrix):
        self._img = None
        self._matrix = matrix

    def with_logo(self, file_path):
        print("Showing game logo...")
        self._img = self._matrix.load_image(file_path)
        self._matrix.object_append(self._img)
        return self

    async def run(self):
        self._matrix.object_remove(self._img)
        font = bitmap_font.load_font("font/MatrixLight8.bdf")
        main_menu = MainMenu(self._matrix, font)
        game_over = GameOver(self._matrix, font)

        phase = Phase.MENU
        game_op = None
        while True:
            self._matrix.clear_display()
            if phase == Phase.MENU:
                game_op = await main_menu.select()
                phase = Phase.GAME_RUNNING
            elif phase == Phase.GAME_RUNNING:
                lost, score = await self._run_game(game_op)
                if lost:
                    self._matrix.clear_display()
                    game_over.set_score(score)
                    phase = await game_over.select()
                else:
                    phase = Phase.MENU

    async def _run_game(self, game_op):
        if game_op is None:
            return
        game = None
        if game_op == GameOption.SNAKE:
            game = sg.Game(self._matrix)
        elif game_op == GameOption.PONG:
            game = pg.Game(self._matrix)
        elif game_op == GameOption.CUBES:
            game = cg.Game(self._matrix)
        await game.run()
        return game.get_world().has_lost(), game.get_world().get_score()

