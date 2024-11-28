
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
        coords = data.split(",")
        coord_z = coords[0].split(":")
        coord_y = coords[1].split(":")
        print(coords)
        z = max(min(int(coord_z[1]), 100), -100)
        y = max(min(int(coord_y[1]), 100), -100)
        State.orientation = (z, y)

        #print("State.orientation = ", State.orientation)
