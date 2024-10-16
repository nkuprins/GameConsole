import asyncio
import matrix
import server

async def main():

    server_task = asyncio.create_task(server.start_server(matrix.update_direction))
    matrix_task = asyncio.create_task(matrix.matrix_scroller())

    try:
        await asyncio.gather(server_task, matrix_task)
    except KeyboardInterrupt:
        server.shutdown_server(server_socket)

asyncio.run(main())
