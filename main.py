import socket
import threading
from server.logger import write_log

class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.pool = threading.Thread(target=self._server)
        self.pool.start()

    def _server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.host, self.port))
        clients_address = []

        print(write_log("Server started"))
        while True:
            data, address = sock.recvfrom(1024)
            if not data:
                break
            if address not in clients_address:
                clients_address.append(address)
                print(write_log(f"Client {clients_address[-1]} has joined"))
            for client_address in clients_address:
                if client_address == address:
                    continue
                sock.sendto(data, client_address)
        sock.close()


if __name__ == '__main__':
    server = Server(host='127.0.0.1', port=9090)