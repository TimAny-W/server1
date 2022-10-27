import sqlite3 as sq
from socket_server.settings import database_path

connection = sq.connect(f'{database_path}/accounts.db')
cursor = sq.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(
    id INT PRIMARY KEY,
    login TEXT NOT NULL,
    password TEXT NOT NULL 
    );
""")
connection.commit()


def cryptographic(data):
    """Encrypts the data
    return encrypted data
    need to realised
    """
    return data


def register_accounts(login, password) -> str:
    """Add account to basedata
    return result of saving
    """

    try:
        cursor.execute("""INSERT INTO accounts VALUES(?, ?);""", cryptographic((login, password)))
        connection.commit()
    except BaseException as ex:

        return f'Account saving error {repr(ex)}'
    else:
        return f'Account was successfully saved'
