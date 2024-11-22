import random

class Color:
    COLORS_COUNT = 7

    BLACK = 0
    LIGHT_GREEN = 1
    DARK_GREEN = 2
    RED = 3
    WHITE = 4
    YELLOW = 5
    BLUE = 6

    _HEX_MAP = {
        BLACK: 0x000000,
        LIGHT_GREEN: 0x3ac766,
        DARK_GREEN: 0x3d6639,
        RED: 0x663b39,
        WHITE: 0xffffff,
        YELLOW: 0xfef65b,
        BLUE: 0x4974a5,
    }

    def colors():
        return Color._HEX_MAP.items()

    def to_hex(color):
        return Color._HEX_MAP.get(color, None)

    def random_color():
        colors = [Color.BLUE, Color.RED, Color.YELLOW, Color.DARK_GREEN]
        index = random.randint(0, len(colors) - 1)
        return colors[index]