import sqlite3 as sq

connection = sq.connect(f'accounts.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(
    id INT PRIMARY KEY,
    login TEXT NOT NULL,
    password TEXT NOT NULL 
    );
""")
connection.commit()


def encrypt_data(data):
    """Encrypts the data
    return encrypted data
    need to realised
    """
    return data


def decrypt_data(data):
    """Decrypts the data
    return decrypted data
    need to realised"""
    return data


def register_accounts(id, login, password) -> str:
    """Add account to database
    return result of saving
    """

    try:
        cursor.execute("""INSERT INTO accounts VALUES(?, ?, ?);""", encrypt_data(id, login, password))
        connection.commit()
    except BaseException as ex:
        return f'Account saving error {repr(ex)}'
    else:
        return f'Account was successfully saved'


def login(login, password):
    """Def of login user
    return True if login and password correct,else
    return False if login and password incorrect
    """
    cursor.execute(f"""SELECT * from accounts WHERE login='{login}'""")
    user = cursor.fetchall()
    if decrypt_data(user[2]) != password:
        return False
    else:
        return True

print(login('tim', 'timany'))
