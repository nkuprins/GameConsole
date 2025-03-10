import asyncio
import adafruit_display_text.label
from properties.constants import HEIGHT, CENTRE_X, CENTRE_Y
from properties.color import Color
from properties.direction import Direction
from properties.state import GameOption

class MainMenu:

    def __init__(self, matrix, font):
        label = adafruit_display_text.label.Label(
            font,
            color=0xff0000,
            text=GameOption.ALL_STR[0])
        label.x = CENTRE_X - 10
        label.y = CENTRE_Y

        self._idx = 0 # game option index
        self._matrix = matrix
        self._label = label


    # Wait for user to choose the game
    # Up or Down change the game option
    # Right selects the game
    async def select(self):
        self._draw()
        await asyncio.sleep(2.0) # let the user process the info

        while True:
            direction = Direction.from_orientation()
            if direction == Direction.UP:
                self._update_idx(self._idx + 1)
                self._label.text = GameOption.ALL_STR[self._idx]
            elif direction == Direction.DOWN:
                self._update_idx(self._idx - 1)
                self._label.text = GameOption.ALL_STR[self._idx]
            elif direction is not None:
                self._clear_label()
                return self._idx

            self._matrix.refresh()
            await asyncio.sleep(1.0) # yield other task

    def _update_idx(self, new_idx):
        limit = len(GameOption.ALL_STR) - 1
        if new_idx > limit:
            new_idx = 0
        elif new_idx < 0:
            new_idx = limit
        self._idx = new_idx

    def _draw(self):
        self._draw_arrow_up()
        self._draw_arrow_down()
        self._draw_label()
        self._matrix.refresh()

    def _draw_arrow_up(self):
        m = self._matrix
        c = Color.RED
        for i in range(8):
            m.draw_pixel(CENTRE_X, i, c)
        for i in range(-3, 4):
            m.draw_pixel(CENTRE_X + i, abs(i), c)

    def _draw_arrow_down(self):
        m = self._matrix
        c = Color.RED
        for i in range(8):
            m.draw_pixel(CENTRE_X, HEIGHT - 1 - i, c)
        for i in range(-3, 4):
            m.draw_pixel(CENTRE_X + i, HEIGHT - 1 - abs(i), c)

    def _draw_label(self):
        self._matrix.object_append(self._label)

    def _clear_label(self):
        self._matrix.object_remove(self._label)
