import board
import displayio
import rgbmatrix
import framebufferio
import asyncio

class Color:
    LIGHT_GREEN = 0
    DARK_GREEN = 1
    RED = 2
    BLACK = 3

class Matrix:
    def __init__(self):
        display = self._setup_display()
        self._display = display
        self._bitmap = displayio.Bitmap(display.width, display.height, 4)
        self._palette = self._setup_palette()
        self._setup_group()
        self.posx = 20
        self.posy = 20
        self.mydirection = "UP"

    def _setup_display(self):
        displayio.release_displays()

        # Setup the RGB matrix
        matrix = rgbmatrix.RGBMatrix(
            width=64, height=32, bit_depth=2,
            rgb_pins=[board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5],
            addr_pins=[board.GP6, board.GP7, board.GP8, board.GP9],
            clock_pin=board.GP10, latch_pin=board.GP11, output_enable_pin=board.GP12)

        display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)
        return display

    def _setup_palette(self):
        palette = displayio.Palette(4)
        palette[Color.LIGHT_GREEN] = 0x3ac766    # Light green background
        palette[Color.DARK_GREEN] =  0x3d6639    # Dark green snake
        palette[Color.RED] =         0x663b39    # Apple
        palette[Color.BLACK] =       0x000000    # Black
        return palette

    def _setup_group(self):
        tile_grid = displayio.TileGrid(self._bitmap, pixel_shader=self._palette)
        group = displayio.Group()
        group.append(tile_grid)
        self._display.root_group = group


    def update_direction(self, direction):
        self.draw_pixel(self.posx, self.posy, Color.DARK_GREEN)
        if direction == "LEFT":
            self.posx -= 1
        elif direction == "RIGHT":
            self.posx += 1
        elif direction == "UP":
            self.posy += 1
        elif direction == "DOWN":
            self.posy -= 1
        self.draw_pixel(self.posx, self.posy, Color.BLACK)
        self.mydirection = direction

    def draw_pixel(self, x, y, color):
        self._bitmap[x, y] = color
        self._display.refresh(minimum_frames_per_second=10)

    def draw_segment(self, pos1, pos2, color):
        for x in range(pos1[0], pos2[0]):
            for y in range(pos1[1], pos2[1]):
                self._bitmap[x, y] = color
        self._display.refresh(minimum_frames_per_second=10)

    def _setup_game(self):
        self.draw_segment((0,0), (self._display.width, self._display.height), Color.DARK_GREEN)
        self.draw_pixel(20, 20, Color.BLACK)

    def run(self):
        self._setup_game()

        while True:
            self.update_direction(self.mydirection)
            await asyncio.sleep(1.0)

