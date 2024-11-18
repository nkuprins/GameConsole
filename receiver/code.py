import asyncio
from gameconsole.matrix import Matrix
import network.server as server
import network.wifi_conn as wifi_conn
import gc
import time
import button_debug.buttons_controller as bc
import board
import gameconsole.state as state
from gameconsole.console import Console

# Circuit python has a very bad garbage collector
# We call it manually to avoid memory leaks of unclosed socket
async def main1():
    gc.enable()

    m = Matrix()
    await asyncio.sleep(1)
    w = wifi_conn.WiFiConnection()
    if not w.connect():
        return


    server_task = asyncio.create_task(
        server.Server(state.update_state).run()
    )
    matrix_task = asyncio.create_task(m.matrix_scroller())

    await asyncio.gather(server_task, matrix_task)
    print("Before collect:", gc.mem_free())
    gc.collect()
    time.sleep(2)
    print("After collect:", gc.mem_free())

async def main2():

    mat = Matrix()
    await asyncio.sleep(1)

    console_task = asyncio.create_task(Console(mat).run())
    controller_task = asyncio.create_task(
        bc.run(bc.create_buttons(), state.update_state)
    )

    await asyncio.gather(controller_task, console_task)

asyncio.run(main2())
