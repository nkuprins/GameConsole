import board
import displayio
import rgbmatrix
import framebufferio
import asyncio
from utility import Color, COLORS_COUNT, WIDTH, HEIGHT, SCALE, BORDER_SIZE

class Matrix:
    
    def __init__(self):

        self._display = self._setup_display()
        self._bitmap = displayio.Bitmap(self._display.width, self._display.height, COLORS_COUNT)
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
        palette = displayio.Palette(COLORS_COUNT)
        palette[Color.LIGHT_GREEN] = Color.LIGHT_GREEN_HEX
        palette[Color.DARK_GREEN]  = Color.DARK_GREEN_HEX
        palette[Color.RED]         = Color.RED_HEX
        palette[Color.BLACK]       = Color.BLACK_HEX
        return palette

    def _setup_group(self):
        tile_grid = displayio.TileGrid(self._bitmap, pixel_shader=self._palette)
        group = displayio.Group()
        group.append(tile_grid)
        self._display.root_group = group

    def draw_pixel(self, x, y, color):
        self._bitmap[x, y] = color

    def draw_with_scale(self, oldpos = None, oldcolor = None, new_pos, new_color):
        def draw_segment(pos, color):
            for x in range(pos[0], pos[0] + SCALE + 1):
                for y in range(pos[1], pos[1] + SCALE + 1):
                    self._bitmap[x, y] = color

        if oldpos is not None and oldcolor is not None:
            draw_segment(oldpos, oldcolor)

        draw_segment(new_pos, new_color)

    def draw_horizontal_line(self, y, color):
        for i in range(WIDTH):
            for j in range(BORDER_SIZE):
                self._matrix.draw_pixel(i, y + j, color)

    def draw_vertical_line(self, x, color):
        for i in range(HEIGHT):
            for j in range(BORDER_SIZE):
                self._matrix.draw_pixel(x + j, i, color)

