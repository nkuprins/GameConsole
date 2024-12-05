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
        label.x = CENTRE_X - 5
        label.y = CENTRE_Y - 5

        self._idx = 0 # game option index
        self._matrix = matrix
        self._label = label


    # Wait for user to choose the game
    # Up or Down change the game option
    # Right selects the game
    async def select(self):
        self._draw()

        while True:
            direction = Direction.from_orientation()
            if direction == Direction.UP:
                self._update_idx(self._idx + 1)
                self._label.text = GameOption.ALL_STR[self._idx]
            elif direction == Direction.DOWN:
                self._update_idx(self._idx - 1)
                self._label.text = GameOption.ALL_STR[self._idx]
            elif direction == Direction.RIGHT:
                self._clear_label()
                return self._idx

            self._matrix.refresh()
            await asyncio.sleep(0.0) # yield other task

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

    def _draw_arrow_up(self):
        m = self._matrix
        c = Color.RED
        for i in range(5):
            m.draw_pixel(CENTRE_X, i, c)
        m.draw_pixel(CENTRE_X - 1, 1, c)
        m.draw_pixel(CENTRE_X - 2, 2, c)
        m.draw_pixel(CENTRE_X + 1, 1, c)
        m.draw_pixel(CENTRE_X + 2, 2, c)

    def _draw_arrow_down(self):
        m = self._matrix
        c = Color.RED
        for i in range(5):
            m.draw_pixel(CENTRE_X, HEIGHT - 1 - i, c)
        m.draw_pixel(CENTRE_X - 1, HEIGHT - 2, c)
        m.draw_pixel(CENTRE_X - 2, HEIGHT - 3, c)
        m.draw_pixel(CENTRE_X + 1, HEIGHT - 2, c)
        m.draw_pixel(CENTRE_X + 2, HEIGHT - 3, c)

    def _draw_label(self):
        self._matrix.object_append(self._label)

    def _clear_label(self):
        self._matrix.object_remove(self._label)
