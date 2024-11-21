import socketpool
import asyncio
import wifi
import time

# Class to run the server
# It opens the server socket, which listens for 1 incoming connection
# It reads from this connection persistently
# Callback function is called on received data
class Server:

    def __init__(self, callback):
        self._server_socket = self._initialize_server()
        self._callback = callback

    # Open the server socket
    def _initialize_server(self):
        pool = socketpool.SocketPool(wifi.radio)
        socket = pool.socket(pool.AF_INET, pool.SOCK_STREAM)
        socket.bind(("0.0.0.0", 80))
        socket.listen(1)
        # We do not want to block the matrix
        socket.setblocking(False)
        if wifi.radio.ipv4_address is None:
            return None
        print("INFO: Server started on ", wifi.radio.ipv4_address)
        return socket

    # Accepts an incoming connection and handles it
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
            time.sleep(2)

    # Closes the client connection if exists
    def _close_client(self, client_socket):
        if client_socket:
            print("INFO: Shutting down the client...")
            client_socket.close()

    def _close_server(self):
        print("INFO: Shutting down the server...")
        self._server_socket.close()

    # Reads from client_socket if can, and calls the callback function
    async def _handle_client(self, client_socket):
        buffer = bytearray(20)
        while True:
            try:
                received = client_socket.recv_into(buffer, 5)
                if received == 0:
                    print("Client disconnected")
                    break

                data = buffer[:received].decode()
                print(data)
                # self._callback(data)
            except OSError as e:
                # No incoming data yet
                if e.args[0] == errno.EAGAIN:
                    # Signal the other task to run
                    await asyncio.sleep(0.1)

    async def _accept_connection(self):
        while True:
            try:
                client_socket, addr = self._server_socket.accept()
                print("INFO: Connection from ", addr)
                return client_socket
            except OSError as e:
                # No incoming connections yet
                if e.args[0] == errno.EAGAIN:
                    # Signal the other task to run
                    await asyncio.sleep(0.1)

