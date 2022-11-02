import socket
import threading
from socket_server.server.database import DBManager

db = DBManager('accs.db')


class Client:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

        self.server = self.host, self.port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.login = ''

        self.sock.bind(('', 0))
        self._init()
        # self.sock.sendto((f'{self.nickname} has joined to server'.encode('utf-8')), self.server)

        self.pool = threading.Thread(target=self._read_sock)
        self.pool.start()

    def _read_sock(self):
        while True:
            data = self.sock.recv(1024)
            print(data.decode('utf-8'))

    def _send_sock(self):
        while True:
            data = input('Write smth: ')
            try:
                self.sock.sendto(
                    f'[{self.login}] {data}\n'.encode('utf-8'),
                    self.server
                )
            except Exception as ex:
                print(repr(ex))

    # ///////////// REGISTRATION ///////////////

    def _init(self):
        choice = int(input("Choice login or register\n login - 1 \n register - 2\n"))
        self.login = input('Write a login: ')
        password = input('Write a password:')

        if choice == 1:
            if not db.login(self.login, password):
                print('Password or login incorrect')
                return self._init()
            else:
                print('Login successfully')
        elif choice == 2:
            if not db.register_account(self.login, password):
                print('Login is not available')
                return self._init()
            else:
                print('Successfully register a new account')

        self._send_sock()
        self._read_sock()


if __name__ == '__main__':
    user = Client(host='127.0.0.1', port=9090)
