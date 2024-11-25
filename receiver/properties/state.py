
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
        coords = data.split("*")
        coord_parts = coords[0].split(",")
        if len(coord_parts) != 2:
            return
        coord_z = coord_parts[0].split(":")
        coord_y = coord_parts[1].split(":")
        if len(coord_z) > 1 and len(coord_y) > 1:
            z = int(coord_z[1])
            y = int(coord_y[1])
            if (z <= 100 or z >= -100) and (y <= 100 or y >= -100):
                State.orientation = (z, y)
                print("We set ", State.orientation)
