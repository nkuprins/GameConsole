import socketpool
import asyncio
import wifi

class Server:

    def __init__(self, callback):
        self._server_socket = self._initialize_server()
        self._callback = callback

    # Open the server socket and listen for 1 incoming connection
    def _initialize_server(self):
        pool = socketpool.SocketPool(wifi.radio)
        socket = pool.socket(pool.AF_INET, pool.SOCK_STREAM)
        socket.bind(("0.0.0.0", 80))
        socket.listen(1)
        socket.setblocking(False)
        if wifi.radio.ipv4_address is None:
            return None
        print("INFO: Server started on ", wifi.radio.ipv4_address)
        return socket

    # Accept an incoming connection and handle it
    async def run(self):
        if self._server_socket is None:
            return

        client_socket = None
        try:
            client_socket = await self._accept_connection()
            await self._handle_client(client_socket)
        except OSError as e:
            print("ERROR: Socket error ", e)
        finally:
            self._close_client(client_socket)
            self._close_server()
            wifi.radio.enabled = False

    async def _accept_connection(self):
        while True:
            try:
                client_socket, addr = self._server_socket.accept()
                print("INFO: Connection from ", addr)
                return client_socket
            except OSError as e:
                if e.args[0] == errno.EAGAIN:
                    await asyncio.sleep(0.0) # yield other task

    # Read from this connection persistently and
    # execute callback function on received data
    async def _handle_client(self, client_socket):

        buffer = bytearray()
        has_started = False
        while True:
            try:
                temp_buffer = bytearray(40)
                received = client_socket.recv_into(temp_buffer, 40)
                if received == 0:
                    print("Client disconnected")
                    break

                last_start = temp_buffer.rfind(b'S')
                last_end = temp_buffer.find(b'E')
                last_end_r = temp_buffer.rfind(b'E')

                if last_start != -1 and last_end_r != -1 and last_start < last_end_r:
                    # [S...E]
                    buffer.clear()
                    buffer.extend(temp_buffer[last_start + 1:last_end_r])
                elif last_start != -1 and \
                        (last_end_r == -1 or (not has_started and last_end_r < last_start)):
                    # [S...]
                    buffer.extend(temp_buffer[last_start + 1:received])
                    has_started = True
                    continue
                elif (last_start == -1 or has_started) and last_end != -1:
                    # [...E]
                    buffer.extend(temp_buffer[:last_end])
                else:
                    # [...]
                    buffer.extend(temp_buffer[:received])
                    continue

                # We can finish but can be more after E
                self._callback(buffer.decode())
                buffer.clear()
                has_started = False
                if last_end_r + 1 < received:
                    has_started = True
                if last_end_r + 2 < received:
                    buffer.extend(temp_buffer[last_end_r + 2:received])
            except OSError as e:
                if e.args[0] == errno.EAGAIN:
                    await asyncio.sleep(0.0) # yield other task

    def _close_client(self, client_socket):
        if client_socket:
            print("INFO: Shutting down the client...")
            client_socket.close()

    def _close_server(self):
        print("INFO: Shutting down the server...")
        self._server_socket.close()