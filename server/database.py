import sqlite3 as sq
import socket_server.server.crypting as crypt


class DBManager:
    def __init__(self, db_name: str):
        self._db_name = db_name

        self._connection = sq.connect(self._db_name)
        self._cursor = self._connection.cursor()

        self.create_table()

    def create_table(self):
        self._cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            login TEXT NOT NULL,
            password TEXT NOT NULL 
            );
        """)
        self._connection.commit()

    def register_account(self, login, password) -> bool:
        self._cursor.execute("SELECT INTO accounts WHERE login=?", )
        self._cursor.execute("INSERT INTO accounts (login, password ) VALUES(?, ?);",
                             crypt.encrypt_data((login, password)))
        self._connection.commit()

    def login(self, login, password):
        self._cursor.execute("SELECT * from accounts WHERE login=?", (login,))
        user = self._cursor.fetchall()
        if crypt.decrypt_data(*user[2]) != password:
            return False  # or raise DBManagerError(e)
        else:
            return True
