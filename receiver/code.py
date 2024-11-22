import asyncio
import gc
import time
import button.buttons_controller as bc
import board
from display.matrix import Matrix
from network.server import Server
from network.custom_wifi import CustomWiFi
from properties.state import State
from core.console import Console

# Main 1 for production
# We manually call garbage collector to avoid memory leaks of unclosed socket,
# as circuit python garbage collector is very bad...
async def main1():
    gc.enable()

    # Set up the matrix and wait
    matrix = Matrix()
    await asyncio.sleep(1)

    # Set up and connect to wifi
    custom_wifi = CustomWiFi()
    if not custom_wifi.connect():
        return

    # Set up the server task to run
    server_task = asyncio.create_task(Server(State.update_orientation).run())
    # Set up the console task to run
    # console_task = asyncio.create_task(Console(matrix).run())

    # Wait for all tasks to complete
    #await asyncio.gather(server_task, console_task)
    await server_task

    print("DEBUG: before collect ", gc.mem_free())
    gc.collect()
    # Wait for sockets to be closed to avoid memory leak
    time.sleep(2)
    print("DEBUG: after collect ", gc.mem_free())

# Main 2 for debugging
async def main2():

    # Set up the matrix and wait
    matrix = Matrix()

    # Set up the console task to run
    console_task = asyncio.create_task(Console(matrix).run())
    # Set up the controller task to run
    controller_task = asyncio.create_task(
        bc.run(bc.create_buttons(), State.update_direction)
    )

    # Wait for all tasks to complete
    await asyncio.gather(controller_task, console_task)

asyncio.run(main1())
