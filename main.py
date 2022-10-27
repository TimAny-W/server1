import socket
import threading
from server.logger import write_log


class Server:
    def __init__(self, host: str, port: int):

        self.host = host
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))

        self.pool = threading.Thread(target=self._server)
        self.pool.start()

        self.clients_address = []

    def _server(self):
        print(write_log("Server started"))
        while True:
            data, address = self.sock.recvfrom(1024)
            self._commands(data, address)
            if not data:
                break
            if address not in self.clients_address:
                self.clients_address.append(address)
                print(write_log(f"Client {self.clients_address[-1]} has joined"))
            for client_address in self.clients_address:
                if client_address == address:
                    continue
                self.sock.sendto(data, client_address)
        self.sock.close()

    def _commands(self, data, address):
        """compares data with exiting commands"""
        self.send_data = 'Connected Users:\n'

        for address in self.clients_address:
            self.send_data += f'{address}\n'

        self.commands = {
            '/tab': self.sock.sendto(self.send_data.encode('utf-8'), address)
        }
        for command in self.commands.keys():
            if command == data:
                self.commands[data]


if __name__ == '__main__':
    try:
        server = Server(host='127.0.0.1', port=9090)
    except BaseException as e:
        write_log(f'Server crashed with error: {}')
