
# Now, since circuit python is a very poor version python,
# we have to do some small workarounds, as there is no enums, staticmethods etc.

COLORS_COUNT = 4
WIDTH = 64
HEIGHT = 32

BORDER_SIZE = 2
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
    match str:
        case "LEFT": return Direction.LEFT
        case "RIGHT": return Direction.RIGHT
        case "UP": return Direction.UP
        case "DOWN": return Direction.DOWN

def to_coord(direction):
    match direction:
        case Direction.LEFT: return (-1, 0)
        case Direction.RIGHT: return (1, 0)
        case Direction.UP: return (0, -1)
        case Direction.DOWN: return (0, 1)