class Phase:
    MENU = 0
    GAME_RUNNING = 1
    GAME_OVER = 2

class GameOption:
    SNAKE = 0
    CUBES = 1
    PONG = 2

class State:
    direction = None
    orientation = (0,0)

    game = None
    phase = Phase.MENU

    def update_direction(direction):
        State.direction = direction

    # Input like: "z:10,y:-10"
    def update_orientation(data):
        coords = data.split(",")
        coord_z = coords[0].split(":")
        coord_y = coords[1].split(":")
        z = int(coord_z[1])
        y = int(coord_y[1])
        State.orientation = (z, y)
        #print("State.orientation = ", State.orientation)
