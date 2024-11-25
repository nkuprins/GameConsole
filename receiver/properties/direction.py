from properties.constants import TRIGGER_ANGLE, WORLD_SIZE
from properties.state import State

class Direction:
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"

    _MAP = {
        "LEFT": LEFT,
        "RIGHT": RIGHT,
        "UP": UP,
        "DOWN": DOWN
    }

    _SPEED_MAP = {
        LEFT: (-1 - WORLD_SIZE, 0),
        RIGHT: (1 + WORLD_SIZE, 0),
        UP: (0, -1 - WORLD_SIZE),
        DOWN: (0, 1 + WORLD_SIZE),
    }

    _OPPOSITE_MAP = {
        RIGHT: LEFT,
        LEFT: RIGHT,
        UP: DOWN,
        DOWN: UP
    }

    _CLOCK_MAP = {
        # =>
        RIGHT: DOWN,
        LEFT: UP,
        # <=
        UP: LEFT,
        DOWN: RIGHT
    }

    def from_string(direction_str):
        return Direction._MAP.get(direction_str, None)

    def from_orientation():
        if State.orientation[0] >= TRIGGER_ANGLE:
            return Direction.LEFT
        elif State.orientation[0] <= -TRIGGER_ANGLE:
            return Direction.RIGHT
        elif State.orientation[1] >= TRIGGER_ANGLE:
            return Direction.UP
        elif State.orientation[1] <= -TRIGGER_ANGLE:
            return Direction.DOWN
        return None

    def to_speed(direction):
        return Direction._SPEED_MAP.get(direction, None)

    def opposite(direction1, direction2):
        if direction1 is None or direction2 is None:
            return
        return direction1 == Direction._OPPOSITE_MAP.get(direction2, None)

    def get_clock_dir(direction):
        return Direction._CLOCK_MAP.get(direction, None)
