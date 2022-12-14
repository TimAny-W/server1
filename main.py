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

    def _server(self):
        print(write_log("Server started"))
        clients_address = []
        while True:
            data, address = self.sock.recvfrom(1024)
            print(address[0], address[1])
            if address not in clients_address:
                clients_address.append(address)
                print(clients_address)
            for clients in clients_address:
                if clients == address:
                    continue
                self.sock.sendto(data, clients)
                print(data, clients)
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
    except BaseException as ex:
        write_log(f'Server crashed with error: {repr(ex)}')
