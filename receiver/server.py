import wifi
import socketpool
import _asyncio

SSID = "NDL_24G"
PASSWORD = "RT-AC66U"

def connect_to_wifi():
    wifi.radio.connect(SSID, PASSWORD)
    print("Connected to", SSID, "IP:", wifi.radio.ipv4_address)

def handle_request(conn):
    buffer = bytearray(1024)
    bytes_received = conn.recv_into(buffer)
    if bytes_received == 0:
        print("No bytes received")
        return
    request = buffer[:bytes_received].decode('utf-8')
    print("Request:", request)

    direction = extract_direction(request)
    if direction:
        self.notify_function(direction)

def extract_direction(self, request):
        if "direction=" in request:
            direction_index = request.find("direction=") + len("direction=")
            direction = request[direction_index:].split(' ')[0].split('&')[0]
            print(f"Direction received: {direction}")
            return direction
        return None

async def process_requests(server_socket, notify_function):
    while True:
        try:
            conn, addr = server_socket.accept()
            print("Connection from", addr)
            handle_request(conn)
        except OSError as e:
            print("Error in process_requests: ", e)
        finally:
            if conn:
                print("Shutting down the client...") # for DEBUG purposes
                conn.close()
            await asyncio.sleep(0.0)

def init_server():
    connect_to_wifi()
    pool = socketpool.SocketPool(wifi.radio)
    server_socket = pool.socket(pool.AF_INET, pool.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 80))
    server_socket.listen(1)
    server_socket.setblocking(False)
    print("Server started on:", wifi.radio.ipv4_address)
    return server_socket

def shutdown_server(server_socket):
    print("Shutting down server...")
    server_socket.close()

async def start_server(notify_function):
    server_socket = init_server()
    await process_requests(server_socket, notify_function)
