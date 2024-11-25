
class Phase:
    MENU = 0
    GAME = 1

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

    def update_orientation(data):
        coords = data.split("*", 1)[0].split(",")
        if len(coords) != 2:
            return

        coord_z = coords[0].split(":")
        coord_y = coords[1].split(":")
        if len(coord_z) > 1:
            z = max(min(int(coord_z[1]), 100), -100)
            State.orientation = (z, State.orientation[1])
        if len(coord_y) > 1:
            y = max(min(int(coord_y[1]), 100), -100)
            State.orientation = (State.orientation[0], y)

        print("State.orientation = ", State.orientation)
