from properties.constants import DEFAULT_TRIGGER_ANGLE, WORLD_SIZE
from properties.state import State

class Direction:
    LEFT =  "LEFT"
    RIGHT = "RIGHT"
    UP =    "UP"
    DOWN =  "DOWN"

    _MAP = {
        "LEFT":  LEFT,
        "RIGHT": RIGHT,
        "UP":    UP,
        "DOWN":  DOWN
    }

    _SPEED_MAP = {
        LEFT:  (-1 - WORLD_SIZE, 0),
        RIGHT: (1 + WORLD_SIZE, 0),
        UP:    (0, -1 - WORLD_SIZE),
        DOWN:  (0, 1 + WORLD_SIZE),
    }

    _OPPOSITE_MAP = {
        RIGHT: LEFT,
        LEFT:  RIGHT,
        UP:    DOWN,
        DOWN:  UP
    }

    def from_string(str):
        return Direction._MAP.get(str, None)

    def from_orientation():
        z, y = State.orientation
        best = max(z, y, key=abs)

        if abs(best) >= DEFAULT_TRIGGER_ANGLE:
            if best == z:
                return Direction.LEFT if z > 0 else Direction.RIGHT
            else:
                return Direction.UP if y > 0 else Direction.DOWN
        return None

    def to_speed(dir):
        return Direction._SPEED_MAP.get(dir, None)

    def is_opposite(dir1, dir2):
        if dir1 is None or dir2 is None:
            return
        return dir1 == Direction._OPPOSITE_MAP.get(dir2, None)
