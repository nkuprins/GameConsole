import asyncio
import adafruit_display_text.label
from properties.direction import Direction
from properties.state import Phase
from properties.constants import HEIGHT

class GameOver:

    def __init__(self, matrix, font):
        score_label = adafruit_display_text.label.Label(
            font,
            color=0xff0000,
            text="SCORE: 0")
        score_label.x = 1
        score_label.y = HEIGHT - 27

        exit_label = adafruit_display_text.label.Label(
            font,
            color=0x0080ff,
            text="LEFT:   EXIT")
        exit_label.x = 1
        exit_label.y = HEIGHT - 15

        restart_label = adafruit_display_text.label.Label(
            font,
            color=0x0080ff,
            text="RIGHT: RESTART")
        restart_label.x = 1
        restart_label.y = HEIGHT - 4

        self._score_label = score_label
        self._exit_label = exit_label
        self._restart_label = restart_label
        self._matrix = matrix

    def set_score(self, score):
        self._score_label.text = "SCORE: " + str(score)

    # Wait for user to choose next phase
    # Left is exit to main menu
    # Right is game restart
    async def select(self):
        self._draw()
        await asyncio.sleep(2.0) # let the user process the info

        while True:
            direction = Direction.from_orientation()
            if direction == Direction.LEFT:
                self._clear()
                return Phase.MENU
            elif direction == Direction.RIGHT:
                self._clear()
                return Phase.GAME_RUNNING

            await asyncio.sleep(0.0) # yield other task

    def _draw(self):
        self._matrix.object_append(self._score_label)
        self._matrix.object_append(self._exit_label)
        self._matrix.object_append(self._restart_label)
        self._matrix.refresh()

    def _clear(self):
        self._matrix.object_remove(self._score_label)
        self._matrix.object_remove(self._exit_label)
        self._matrix.object_remove(self._restart_label)
        self._matrix.refresh()

