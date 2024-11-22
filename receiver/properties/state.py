
class State:
    direction = None
    orientation = (0,0)

    game = None
    phase = Phase.MENU

    def update_direction(direction):
        State.direction = direction

    def update_orientation(str):
        parts = data.split(",")
        z = int(parts[0].split(":")[1])
        y = int(parts[1].split(":")[1])
        State.orientation = (z, y)


class GameOption:
    SNAKE = 0
    CUBES = 1
    PONG = 2

class Phase:
    MENU = 0
    GAME = 1