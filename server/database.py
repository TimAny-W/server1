import sqlite3 as sq
import socket_server.server.crypting as crypt


class DBManager:
    def __init__(self, db_name: str):
        self._db_name = db_name

        self._connection = sq.connect(f'./{self._db_name}')
        self._cursor = self._connection.cursor()

        self._create_table()

    def _create_table(self):
        self._cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            login TEXT NOT NULL,
            password TEXT NOT NULL 
            );
        """)
        self._connection.commit()

    def register_account(self, login, password) -> bool:
        """Register a new account in system"""
        if self._check_is_login_available(login):
            self._cursor.execute("INSERT INTO accounts (login, password ) VALUES(?, ?);",
                                 crypt.encrypt_data((login, password)))
            self._connection.commit()
            return True
        else:
            return False

    def _check_is_login_available(self, login) -> bool:
        """checking login is available"""
        self._cursor.execute("SELECT * FROM accounts WHERE login=?", (login,))
        all_logins = self._cursor.fetchall()
        if all_logins == []:
            return True
        else:
            return False

    def login(self, login, password) -> bool:
        """login in a system"""
        self._cursor.execute("SELECT * from accounts WHERE login=?", (login,))

        user = self._cursor.fetchone()
        print(user)
        if user == ():
            print('No found users with this login')
        if crypt.decrypt_data(user[2]) != password:
            return False  # or raise DBManagerError(e)
        else:
            return True
