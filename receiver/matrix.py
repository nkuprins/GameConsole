import board
import displayio
import rgbmatrix
import adafruit_display_text.label
import terminalio
import framebufferio
import asyncio
import time

def start():
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

def update_direction(direction):
    line1.text = f"Direction: {direction}"

async def scroll(line):
    line.x = line.x - 1
    line_width = line.bounding_box[2]
    if line.x < -line_width:
        line.x = display.width
    await asyncio.sleep(0.01)

async def matrix_scroller():
    isCalled = False
    while True:
        await scroll(line1)
        display.refresh(minimum_frames_per_second=0)
        await asyncio.sleep(0.0)

#while True:
#    scroll(line1)
#    display.refresh(minimum_frames_per_second=0)
#    time.sleep(0.01)
