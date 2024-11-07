import asyncio
import matrix
import server
import wifi_conn
import gc
import time

async def main():
    return
    gc.enable()

    m = matrix.Matrix()
    await asyncio.sleep(2)
    w = wifi_conn.WiFiConnection()
    if not w.connect():
        return


    server_task = asyncio.create_task(
        server.Server(m.update_direction).run()
    )
    matrix_task = asyncio.create_task(m.matrix_scroller())

    await asyncio.gather(server_task, matrix_task)
    print("Before collect:", gc.mem_free())
    gc.collect()
    time.sleep(2)
    print("After collect:", gc.mem_free())


asyncio.run(main())
