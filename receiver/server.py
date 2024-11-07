import socketpool
import asyncio
import wifi
import time

class Server:

    def __init__(self, notify_function):
        self._server_socket = self._initialize_server()
        self._notify_function = notify_function

    def _initialize_server(self):
        pool = socketpool.SocketPool(wifi.radio)
        socket = pool.socket(pool.AF_INET, pool.SOCK_STREAM)
        socket.bind(("0.0.0.0", 80))
        socket.listen(1)
        socket.setblocking(False)
        print("Server started on ", wifi.radio.ipv4_address)
        if wifi.radio.ipv4_address is None:
            return None
        return socket

    def _close_client(self, client_socket):
        if client_socket:
            print("Shutting down the client...")
            client_socket.close()

    def _close_server(self):
        print("Shutting down server...")
        self._server_socket.close()

    async def _handle_client(self, client_socket):
        buffer = bytearray(5)
        while True:
            try:
                received = client_socket.recv_into(buffer, 5)
                if received == 0:
                    print("Client disconnected")
                    break

                data = buffer[:received].decode()
                self._notify_function(data)
            except OSError as e:
                if e.args[0] == errno.EAGAIN:
                    await asyncio.sleep(0.1)

    async def _accept_connection(self):
        while True:
            try:
                client_socket, addr = self._server_socket.accept()
                print("Connection from ", addr)
                return client_socket
            except OSError as e:
                if e.args[0] == errno.EAGAIN:
                    await asyncio.sleep(0.1)

    async def run(self):
        if self._server_socket is None:
            return

        client_socket = None

        try:
            client_socket = await self._accept_connection()
            await self._handle_client(client_socket)
        except OSError as e:
            print("Socket error ", e)
        finally:
            self._close_client(client_socket)
            self._close_server()
            wifi.radio.enabled = False
            time.sleep(2)
