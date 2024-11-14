import asyncio
import matrix
import server
import wifi_conn
import gc
import time
import button
import board

async def main1():
    gc.enable()

    m = matrix.Matrix()
    await asyncio.sleep(1)
    w = wifi_conn.WiFiConnection()
    if not w.connect():
        return


    server_task = asyncio.create_task(
        server.Server(m.update_direction).run()
    )
    matrix_task = asyncio.create_task(m.matrix_scroller())
    controller_task = asyncio.create_task(controller(m.update_direction))

    await asyncio.gather(controller_task, matrix_task)
    print("Before collect:", gc.mem_free())
    gc.collect()
    time.sleep(2)
    print("After collect:", gc.mem_free())

async def main2():
    gc.enable()

    m = matrix.Matrix()
    await asyncio.sleep(1)

    left_btn = button.Button(board.GP18, m.update_direction, "LEFT")
    right_btn = button.Button(board.GP22, m.update_direction, "RIGHT")
    up_btn = button.Button(board.GP27, m.update_direction, "UP")
    down_btn = button.Button(board.GP28, m.update_direction, "DOWN")
    buttons = [left_btn, right_btn, up_btn, down_btn]

    matrix_task = asyncio.create_task(m.run())
    controller_task = asyncio.create_task(controller(buttons))

    await asyncio.gather(controller_task, matrix_task)

async def controller(buttons):
    while True:
        for button in buttons:
            button.handle()
        await asyncio.sleep(0.0)


asyncio.run(main2())

