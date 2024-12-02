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
                    # Signal the other task to run
                    await asyncio.sleep(0.0)

    # Read from this connection persistently and
    # execute callback function on received data
    async def _handle_client(self, client_socket):
        while True:
            try:
                temp_buffer = bytearray(100)
                received = client_socket.recv_into(temp_buffer, 100)
                if received == 0:
                    print("Client disconnected")
                    break

                # Star sign is a delimiter for data
                last_index = temp_buffer.rindex(b'*')
                second_last_index = temp_buffer.rfind(b'*', 0, last_index)

                if second_last_index != -1 and last_index != second_last_index:
                    full_message = temp_buffer[second_last_index + 1:last_index].decode()
                    self._callback(full_message)
            except OSError as e:
                if e.args[0] == errno.EAGAIN:
                    # Signal the other task to run
                    await asyncio.sleep(0.0)

    def _close_client(self, client_socket):
        if client_socket:
            print("INFO: Shutting down the client...")
            client_socket.close()

    def _close_server(self):
        print("INFO: Shutting down the server...")
        self._server_socket.close()