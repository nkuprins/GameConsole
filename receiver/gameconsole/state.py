from utility import Direction

class GameOption:
    SNAKE = 0
    CUBES_FALL = 1

class Phase:
    MENU = 0
    GAME = 1

class State:
    DIRECTION = None
    PHASE = Phase.MENU
    GAME = None

def update_state(direction):
    State.DIRECTION = direction
