import adafruit_display_text.label
from adafruit_bitmap_font import bitmap_font

class GameOver:

    def __init__(self, matrix):

        font = bitmap_font.load_font("font/MatrixLight8.bdf")

        score_label = adafruit_display_text.label.Label(
            font,
            color=0xff0000,
            text="SCORE: 999")
        score_label.x = 1
        score_label.y = 5

        exit_label = adafruit_display_text.label.Label(
            font,
            color=0x0080ff,
            text="LEFT:   EXIT")
        exit_label.x = 1
        exit_label.y = 17

        restart_label = adafruit_display_text.label.Label(
            font,
            color=0x0080ff,
            text="RIGHT: RESTART")
        restart_label.x = 1
        restart_label.y = 28

        self._score_label = score_label
        self._exit_label = exit_label
        self._restart_label = restart_label
        self._matrix = matrix
        
    def draw(self):
        self._matrix.object_append(self._score_label)
        self._matrix.object_append(self._exit_label)
        self._matrix.object_append(self._restart_label)

    def clear(self):
        self._matrix.object_remove(self._score_label)
        self._matrix.object_remove(self._exit_label)
        self._matrix.object_remove(self._restart_label)
