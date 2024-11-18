
# Now, since circuit python is a very poor version python,
# we have to do some small workarounds, as there is no enums, staticmethods etc.

COLORS_COUNT = 4
WIDTH = 64
HEIGHT = 32

BORDER_SIZE = 1
SCALE = 1

class Color:
    LIGHT_GREEN = 0
    DARK_GREEN = 1
    RED = 2
    BLACK = 3
    LIGHT_GREEN_HEX = 0x3ac766
    DARK_GREEN_HEX = 0x3d6639
    RED_HEX = 0x663b39
    BLACK_HEX = 0x000000

class Direction:
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"

def string_to_direction(str):
    if str == "LEFT":
        return Direction.LEFT
    elif str == "RIGHT":
        return Direction.RIGHT
    elif str == "UP":
        return Direction.UP
    elif str == "DOWN":
        return Direction.DOWN

    return None

def to_coord(direction):
    if direction == Direction.LEFT:
        return (-1 - SCALE, 0)
    elif direction == Direction.RIGHT:
        return (1 + SCALE, 0)
    elif direction == Direction.UP:
        return (0, -1 - SCALE)
    elif direction == Direction.DOWN:
        return (0, 1 + SCALE)

    return None
