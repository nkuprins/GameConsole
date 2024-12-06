from properties.color import Color

# For controller
DEFAULT_TRIGGER_Z = 20
DEFAULT_TRIGGER_Y = 13

# For the snake game
SNAKE_GAME_DELAY = 0.6
SNAKE_HEAD_COLOR = Color.BLUE
SNAKE_BODY_COLOR = Color.DARK_GREEN
SNAKE_FOOD_COLOR = Color.RED

# For the pong game
PONG_GAME_DELAY = 0.25
PONG_PLATFORM_DELAY = 0.2
PONG_PLATFORM_SIZE = 3
PONG_PLATFORM_COLOR = Color.WHITE
PONG_BALL_COLOR = Color.WHITE

# For the cubes game
CUBES_TRIGGER_Z = 20
CUBES_TRIGGER_Y = 10
CUBES_GAME_SIZE = 4
CUBES_TIMEOUT = 10.0

# For the matrix
WIDTH = 64
HEIGHT = 32
CENTRE_X = int(WIDTH / 2)
CENTRE_Y = int(HEIGHT / 2)

# If size is 0, then the world has a default size, which is 1 pixel for main objects
# For example, snake body part and head will be 1x1
# If size is n and n > 0, then the world has a scaled size, which is 1+n pixel for main objects
# For example, if n=1 then snake body part and head will be 2x2
WORLD_SIZE = 1

