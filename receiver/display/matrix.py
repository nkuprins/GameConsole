import board
import displayio
import rgbmatrix
import framebufferio
from properties.constants import WIDTH, HEIGHT, WORLD_SIZE
from properties.direction import Direction
from properties.color import Color

# Class to set up the matrix and draw pixels
class Matrix:

    def __init__(self):
        self._display = self._setup_display()
        self._group = displayio.Group()
        self._display.root_group = self._group
        self._bitmap = displayio.Bitmap(self._display.width, self._display.height, Color.COLORS_COUNT)
        self._palette = self._setup_palette()
        # Initial tile
        tile_grid = displayio.TileGrid(self._bitmap, pixel_shader=self._palette)
        self.object_append(tile_grid)

    def _setup_display(self):
        # To avoid screen not released bugs
        displayio.release_displays()

        matrix = rgbmatrix.RGBMatrix(
            width=WIDTH, height=HEIGHT, bit_depth=2,
            rgb_pins=[board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5],
            addr_pins=[board.GP6, board.GP7, board.GP8, board.GP9],
            clock_pin=board.GP10, latch_pin=board.GP11, output_enable_pin=board.GP12)

        return framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

    def _setup_palette(self):
        palette = displayio.Palette(Color.COLORS_COUNT)
        for id, value in Color.colors():
            palette[id] = value
        return palette

    # Note: not tested yet
    def load_image(self, file_path):
        disk_bitmap = displayio.OnDiskBitmap(file_path)
        return displayio.TileGrid(disk_bitmap, pixel_shader=displayio.ColorConverter())

    def object_append(self, obj):
        self._group.append(obj)

    def object_remove(self, obj):
        if obj is not None:
            self._group.remove(obj)

    def has_color(self, x, y, color):
        if 0 <= x <= WIDTH - 1 and 0 <= y <= HEIGHT - 1:
            return self._bitmap[x, y] == color
        return False

    def refresh(self):
        self._display.refresh()

    # Draws a pixel at (x,y) point with color
    def draw_pixel(self, x, y, color):
        self._bitmap[x, y] = color

    # Draws a square with (WORLD_SIZE + 1) width/height
    def draw_square(self, top_left, color):
        self.draw_custom_square(top_left, WORLD_SIZE, color)

    # Draws a square with (size + 1) width/height
    def draw_custom_square(self, top_left, size, color):
        for x in range(top_left[0], top_left[0] + size + 1):
            for y in range(top_left[1], top_left[1] + size + 1):
                self.draw_pixel(x, y, color)

    # Draws rectangle with number of squares and direction down or right
    def draw_rectangle(self, top_left, squares_num, color, direction):
        x_move = 0
        y_move = 0
        if direction == Direction.DOWN:
            y_move = WORLD_SIZE + 1
        elif direction == Direction.RIGHT:
            x_move = WORLD_SIZE + 1
        else:
            return

        for i in range(squares_num):
            new_pos = (top_left[0] + i * x_move, top_left[1] + i * y_move)
            self.draw_square(new_pos, color)

    # Draws pixels for WIDTH and HEIGHT with color
    def draw_background(self, color):
        for x in range(0, WIDTH):
            for y in range(0, HEIGHT):
                self.draw_pixel(x, y, color)

    def clear_display(self):
        self.draw_background(Color.BLACK)

    # Draws a horizontal line at y coordinate with scaling factor
    def draw_horizontal_line(self, y, color):
        for i in range(WIDTH):
            for j in range(WORLD_SIZE + 1):
                self.draw_pixel(i, y + j, color)

    # Draws a vertical line at x coordinate with scaling factor
    def draw_vertical_line(self, x, color):
        for i in range(HEIGHT):
            for j in range(WORLD_SIZE + 1):
                self.draw_pixel(x + j, i, color)

    def draw_border(self, color):
        self.draw_horizontal_line(0, color)
        self.draw_horizontal_line(HEIGHT - WORLD_SIZE - 1, color)
        self.draw_vertical_line(0, color)
        self.draw_vertical_line(WIDTH - WORLD_SIZE - 1, color)