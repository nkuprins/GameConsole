import asyncio
import matrix
import server
import wifi_conn
import gc
import time

async def main():
    gc.enable()

    wifi_conn = WiFiConnection
    if not wifi_conn.connect():
        return

    server_task = asyncio.create_task(
        server.Server(matrix.update_direction).run()
    )
    matrix_task = asyncio.create_task(matrix.matrix_scroller())

    await asyncio.gather(server_task, matrix_task)

    print("Before collect:", gc.mem_free())
    gc.collect()
    time.sleep(2)
    print("After collect:", gc.mem_free())


asyncio.run(main())
