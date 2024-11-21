import board
import displayio
import rgbmatrix
import framebufferio
import asyncio
from utility import Color, WIDTH, HEIGHT, SCALE

# Class to setup the matrix and draw pixels
class Matrix:

    def __init__(self):
        self._display = self._setup_display()
        self._bitmap = displayio.Bitmap(self._display.width, self._display.height, Color.COLORS_COUNT)
        self._palette = self._setup_palette()
        self._setup_group()

    def _setup_display(self):
        displayio.release_displays()

        # Setup the RGB matrix
        matrix = rgbmatrix.RGBMatrix(
            width=WIDTH, height=HEIGHT, bit_depth=2,
            rgb_pins=[board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5],
            addr_pins=[board.GP6, board.GP7, board.GP8, board.GP9],
            clock_pin=board.GP10, latch_pin=board.GP11, output_enable_pin=board.GP12)

        display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)
        return display

    def _setup_palette(self):
        palette = displayio.Palette(Color.COLORS_COUNT)
        palette[Color.LIGHT_GREEN] = Color.to_hex(LIGHT_GREEN)
        palette[Color.DARK_GREEN]  = Color.to_hex(DARK_GREEN)
        palette[Color.RED]         = Color.to_hex(RED)
        palette[Color.BLACK]       = Color.to_hex(BLACK)
        palette[Color.WHITE]       = Color.to_hex(WHITE)
        palette[Color.YELLOW]      = Color.to_hex(YELLOW)
        palette[Color.BLUE]        = Color.to_hex(BLUE)
        return palette

    def _setup_group(self):
        tile_grid = displayio.TileGrid(self._bitmap, pixel_shader=self._palette)
        group = displayio.Group()
        group.append(tile_grid)
        self._display.root_group = group

    # Draws a pixel at (x,y) point with color 
    def draw_pixel(self, x, y, color):
        self._bitmap[x, y] = color

    # Draws a pixel at pos with color 
    # If clean_pos and clean_color are not none,
    # then also draws a pixel for cleaning at clean_pos with clean_color
    def draw_pixel_(self, pos, color, clean_pos = None, clean_color = None):
        if clean_pos is not None and clean_color is not None:
            self.draw_pixel(clean_pos[0], clean_pos[1], clean_color)
        self.draw_pixel(pos[0], pos[1], color)

    # Draws a segment at pos with color
    # If clean_pos and clean_color are not none,
    # then also draws a segment for cleaning at clean_pos with clean_color
    def draw_with_scale(self, pos, color, clean_pos = None, clean_color = None):
        # Draws pixels with scaling factor included (2x2, 3x3...)
        def draw_segment(p, c):
            for x in range(p[0], p[0] + SCALE + 1):
                for y in range(p[1], p[1] + SCALE + 1):
                    self.draw_pixel(x, y, c)

        if clean_pos is not None and clean_color is not None:
            draw_segment(clean_pos, clean_color)

        draw_segment(pos, color)

    # Draws pixels for WIDTH and HEIGHT with color
    def draw_background(self, color):
        for x in range(0, WIDTH):
            for y in range(0, HEIGHT):
                self.draw_pixel(x, y, color)

    # Draws a horizontal line at y coordinate with scaling factor
    def draw_horizontal_line(self, y, color):
        for i in range(WIDTH):
            for j in range(SCALE):
                self.draw_pixel(i, y + j, color)

    # Draws a vertical line at x coordinate with scaling factor
    def draw_vertical_line(self, x, color):
        for i in range(HEIGHT):
            for j in range(SCALE):
                self.draw_pixel(x + j, i, color)

    def draw_border(self, color):
        self.draw_horizontal_line(0, color)
        self.draw_horizontal_line(HEIGHT - SCALE - 1, color)
        self.draw_vertical_line(0, color)
        self.draw_vertical_line(WIDTH - BORDER_SIZE - 1, color)

    def has_color(self, x, y, color):
        return self._bitmap[x, y] == color
