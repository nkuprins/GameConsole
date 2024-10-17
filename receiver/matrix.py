import board
import displayio
import rgbmatrix
import adafruit_display_text.label
import terminalio
import framebufferio

displayio.release_displays()

# Setup the RGB matrix
matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=1,
    rgb_pins=[board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5],
    addr_pins=[board.GP6, board.GP7, board.GP8, board.GP9],
    clock_pin=board.GP10, latch_pin=board.GP11, output_enable_pin=board.GP12)

display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

line1 = adafruit_display_text.label.Label(
    terminalio.FONT, text="Direction:", color=0xFF0000)
line1.x = 0
line1.y = 10

g = displayio.Group()
g.append(line1)
display.root_group = g

def update_direction(direction):
    line1.text = f"Direction: {direction}"
    display.refresh()

async def matrix_scroller():
    while True:
        await asyncio.sleep(1)
