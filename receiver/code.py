import asyncio
import gc
import board
import buttons.buttons_controller as bc
from display.matrix import Matrix
from network.server import Server
from network.custom_wifi import CustomWiFi
from properties.state import State
from core.console import Console

# Main 1 for production
# Note: we manually call garbage collector to avoid memory leaks of unclosed socket,
# as circuit python garbage collector is very bad...
async def main1():
    gc.enable()

    # Set up the matrix
    matrix = Matrix()
    # Set up the console
    console = Console(matrix).with_logo("/img/console_logo.bmp")

    # Set up and try to connect to Wi-Fi
    custom_wifi = CustomWiFi()
    if not custom_wifi.connect():
        return

    # Set up the server
    server_task = asyncio.create_task(Server(State.update_orientation).run())
    # Run the console
    console_task = asyncio.create_task(console.run())

    await asyncio.gather(server_task, console_task)

    gc.collect()
    # Wait for sockets to be closed to avoid memory leak
    await asyncio.sleep(2.0)

# Main 2 for debugging
async def main2():

    # Set up the matrix
    matrix = Matrix()

    # Set up the console
    console_task = asyncio.create_task(Console(matrix).run())
    # Set up the buttons
    controller_task = asyncio.create_task(
        bc.run(bc.create_buttons(), State.update_direction)
    )

    await asyncio.gather(controller_task, console_task)

asyncio.run(main1())
