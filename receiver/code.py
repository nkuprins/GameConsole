# SPDX-FileCopyrightText: 2020 Jeff Epler for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# This example implements a simple two line scroller using
# Adafruit_CircuitPython_Display_Text. Each line has its own color
# and it is possible to modify the example to use other fonts and non-standard
# characters.

import adafruit_display_text.label
import board
import displayio
import framebufferio
import rgbmatrix
import terminalio
import wifi
import socketpool
import time
import select

SSID = "NDL_24G"
PASSWORD = "RT-AC66U"

# Function to connect to Wi-Fi with error handling
def connect_to_wifi():
    max_retries = 5
    attempt = 0
    while attempt < max_retries:
        try:
            print(f"Connecting to WiFi... Attempt {attempt + 1}/{max_retries}")
            wifi.radio.connect(SSID, PASSWORD)
            print("Connected, IP address:", wifi.radio.ipv4_address)
            return True
        except ConnectionError as e:
            print(f"Connection failed: {e}")
            attempt += 1
            time.sleep(2)  # Wait before retrying

    print("Failed to connect to WiFi after multiple attempts.")
    return False

# Try to connect to Wi-Fi
if not connect_to_wifi():
    raise RuntimeError("Could not connect to Wi-Fi, check credentials or network status.")


# Start a simple server
pool = socketpool.SocketPool(wifi.radio)
server = pool.socket(pool.AF_INET, pool.SOCK_STREAM)

# Bind to all available interfaces (0.0.0.0) on port 80
server.bind(("0.0.0.0", 80))
server.listen(1)
server.settimeout(0.1)  # Set the server socket to non-blocking with a timeout of 0.1 seconds
print("Listening on http://%s" % wifi.radio.ipv4_address)

# If there was a display before (protomatter, LCD, or E-paper), release it so
# we can create ours
displayio.release_displays()

# This next call creates the RGB Matrix object itself. It has the given width
# and height. bit_depth can range from 1 to 6; higher numbers allow more color
# shades to be displayed, but increase memory usage and slow down your Python
# code. If you just want to show primary colors plus black and white, use 1.
# Otherwise, try 3, 4 and 5 to see which effect you like best.
#
# These lines are for the Feather M4 Express. If you're using a different board,
# check the guide to find the pins and wiring diagrams for your board.
# If you have a matrix with a different width or height, change that too.
# If you have a 16x32 display, try with just a single line of text.
matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=1,
    rgb_pins=[board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5],
    addr_pins=[board.GP6, board.GP7, board.GP8, board.GP9],
    clock_pin=board.GP10, latch_pin=board.GP11, output_enable_pin=board.GP12)

# Associate the RGB matrix with a Display so that we can use displayio features
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

# Create two lines of text to scroll. Besides changing the text, you can also
# customize the color and font (using Adafruit_CircuitPython_Bitmap_Font).
# To keep this demo simple, we just used the built-in font.
# The Y coordinates of the two lines were chosen so that they looked good
# but if you change the font you might find that other values work better.
line1 = adafruit_display_text.label.Label(
    terminalio.FONT,
    color=0xff0000,
    text="This scroller is brought to you by CircuitPython RGBMatrix")
line1.x = display.width
line1.y = 8

line2 = adafruit_display_text.label.Label(
    terminalio.FONT,
    color=0x0080ff,
    text="Hello to all CircuitPython contributors worldwide <3")
line2.x = display.width
line2.y = 24

# Put each line of text into a Group, then show that group.
g = displayio.Group()
g.append(line1)
g.append(line2)
display.root_group = g

# This function will scoot one label a pixel to the left and send it back to
# the far right if it's gone all the way off screen. This goes in a function
# because we'll do exactly the same thing with line1 and line2 below.
def scroll(line):
    line.x = line.x - 1
    line_width = line.bounding_box[2]
    if line.x < -line_width:
        line.x = display.width

# This function scrolls lines backwards.  Try switching which function is
# called for line2 below!
def reverse_scroll(line):
    line.x = line.x + 1
    line_width = line.bounding_box[2]
    if line.x >= display.width:
        line.x = -line_width

# You can add more effects in this loop. For instance, maybe you want to set the
# color of each label to a different value.
while True:
    scroll(line1)
    scroll(line2)
    #reverse_scroll(line2)
    display.refresh(minimum_frames_per_second=0)

    try:
        conn, addr = server.accept()  # Non-blocking with timeout
        print("Connection from", addr)

        # Use recv_into to receive data into a buffer
        buffer = bytearray(1024)
        bytes_received = conn.recv_into(buffer)  # Use recv_into to fill the buffer with data
        request = buffer[:bytes_received].decode('utf-8')
        print("Request:", request)

        # Handle request and toggle LED
        if "GET /" in request:
            # Find the 'direction' parameter from the URL
            if "direction=" in request:
                direction_index = request.find("direction=") + len("direction=")
                direction = request[direction_index:].split(' ')[0].split('&')[0]
                print(f"Direction received: {direction}")

            # Respond to the client
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nDirection received!"
            conn.send(response.encode('utf-8'))
        conn.close()

    except OSError as e:
        # If no connection was made, continue the loop
        pass
# Write your code here :-)
