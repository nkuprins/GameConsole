
# For the network
SSID = "NDL_24G"
WIFI_PSWD = "RT-AC66U"

# For the matrix
WIDTH = 64
HEIGHT = 32
# If scale is 0, then the world has a default size, which is 1 pixel for main objects
# For example, snake body part and head will be 1x1
# If scale is n and n > 0, then the world has a scaled size, which is 1+n pixel for main objects
# For example, if n=1 then snake body part and head will be 2x2 
SCALE = 1

# For the cubes game
CUBES_SENSITIVITY = 10
CUBES_SIZE = 1

class Color:
    COLORS_COUNT = 7

    LIGHT_GREEN = 0
    DARK_GREEN = 1
    RED = 2
    BLACK = 3
    WHITE = 4
    YELLOW = 5
    BLUE = 6

    def to_hex(color):
        if color == Color.LIGHT_GREEN: return 0x3ac766
        elif color == Color.DARK_GREEN: return 0x3d6639
        elif color == Color.RED: return 0x663b39
        elif color == Color.BLACK: return 0x000000
        elif color == Color.WHITE: return 0xffffff
        elif color == Color.WHITE: return 0xfef65b 
        elif color == Color.BLUE: return 0x4974a5 
        return None

class Direction:
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"

    def from_string(str):
        if str == "LEFT": return Direction.LEFT
        elif str == "RIGHT": return Direction.RIGHT
        elif str == "UP": return Direction.UP
        elif str == "DOWN": return Direction.DOWN
        return None

    # Takes direction and returns the movement point
    # with scaling factor included
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

