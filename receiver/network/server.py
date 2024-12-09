import socketpool
import asyncio
import wifi

class Server:

    def __init__(self, callback):
        self._server_socket = self._initialize_server()
        self._callback = callback

    # Initialize the UDP server socket
    def _initialize_server(self):
        pool = socketpool.SocketPool(wifi.radio)
        socket = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)
        socket.bind(("0.0.0.0", 50000))
        print("INFO: UDP Server started on ", wifi.radio.ipv4_address)
        return socket

    # Run the UDP server
    async def run(self):
        if self._server_socket is None:
            return
        try:
            while True:
                buffer = bytearray(100)
                received = self._server_socket.recvfrom_into(buffer)
                if received != 0:
                    last_start = buffer.rfind(b'S')
                    last_end = buffer.rfind(b'E')
                    if last_start != -1 and last_end != -1:
                        #print(buffer[last_start + 1:last_end].decode())
                        self._callback(buffer[last_start + 1:last_end].decode())
                await asyncio.sleep(0.1)
        except OSError as e:
            print("ERROR: Socket error ", e)
        finally:
            self._close_server()

    def _handle_client(self):
        print("in function reading")
        try:
            buffer = bytearray(100)
            received = self._server_socket.recvfrom_into(buffer)
            if received != 0:
                last_start = buffer.rfind(b'S')
                last_end = buffer.rfind(b'E')
                if last_start != -1 and last_end != -1:
                    self._callback(buffer[last_start + 1:last_end].decode())
            await asyncio.sleep(0.0)
        except OSError as e:
            print("ERROR: Socket error ", e)
            await asyncio.sleep(0.0)


    def _close_server(self):
        print("INFO: Shutting down the UDP server...")
        self._server_socket.close()
