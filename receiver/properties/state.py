class Phase:
    MENU = 0
    GAME_RUNNING = 1

class GameOption:
    SNAKE = 0
    PONG = 1
    CUBES = 2
    ALL_STR = ["SNAKE", "PONG", "CUBES"]

class State:
    direction = None
    orientation = (0,0)

    def update_direction(direction):
        State.direction = direction

    # Input like: "z:10,y:-10"
    def update_orientation(data):
        try:
            coords = data.split(",")
            coord_z = coords[0].split(":")
            coord_y = coords[1].split(":")
            z = int(coord_z[1])
            y = int(coord_y[1])
            State.orientation = (z, y)
            #print("State.orientation = ", State.orientation)
        except (IndexError, ValueError) as e:
            print("ERROR: updating orientation: {e}")

