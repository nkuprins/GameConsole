class GameOption:
    SNAKE = 0
    CUBES_FALL = 1
    PONG = 2

class Phase:
    MENU = 0
    GAME = 1

class State:
    direction = None
    game = None
    phase = Phase.MENU

    def update_direction(direction):
        State.direction = direction
