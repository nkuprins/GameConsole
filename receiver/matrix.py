import board
import displayio
import rgbmatrix
import adafruit_display_text.label
import terminalio
import framebufferio
import asyncio
import time

class Matrix:
    def __init__(self):
        t = self._start()
        self._line1 = t[0]
        self._display = t[1]

    def _start(self):
        displayio.release_displays()

        # Setup the RGB matrix
        matrix = rgbmatrix.RGBMatrix(
            width=64, height=32, bit_depth=1,
            rgb_pins=[board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5],
            addr_pins=[board.GP6, board.GP7, board.GP8, board.GP9],
            clock_pin=board.GP10, latch_pin=board.GP11, output_enable_pin=board.GP12)

        display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

        line1 = adafruit_display_text.label.Label(
            terminalio.FONT,
            color=0xff0000,
            text="Direction: No")
        line1.x = 0
        line1.y = 8

        g = displayio.Group()
        g.append(line1)
        display.root_group = g
        display.refresh(minimum_frames_per_second=0)
        return line1, display

    def update_direction(self, direction):
        self._line1.text = f"Direction: {direction}"

    async def _scroll(self, line):
        line.x = line.x - 1
        line_width = line.bounding_box[2]
        if line.x < -line_width:
            line.x = self._display.width
        await asyncio.sleep(0.01)

    async def matrix_scroller(self):
        isCalled = False
        print("START MATRIX")
        while True:
            await self._scroll(self._line1)
            self._display.refresh(minimum_frames_per_second=0)
            await asyncio.sleep(0.0)

#while True:
#    scroll(line1)
#    display.refresh(minimum_frames_per_second=0)
#    time.sleep(0.01)
