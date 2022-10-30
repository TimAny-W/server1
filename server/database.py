import sqlite3 as sq

class DBManagerError(Exception):
    pass

class DBManager:
    def __init__(self, db_name: str):
        self._db_name = db_name
        
    def open() -> bool:         
        try:
           self._connection = sq.connect(self._db_name)
           self._cursor = connection.cursor()
           return True 
        except some_sqlite_exception:
           return False 
    
    def create_table(self):
        self._cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(
            id INT PRIMARY KEY,
            login TEXT NOT NULL,
            password TEXT NOT NULL 
            );
        """)
        self._connection.commit()


    def register_accounts(self, id, login, password) -> bool:
        try:
            self._cursor.execute("INSERT INTO accounts VALUES(?, ?, ?);", encrypt_data(id, login, password))
            self._connection.commit()
        except some_sqlite_exception as ex:
            return True  # or raise DBManagerError(e)
        else:
            return False


    def login(self, login, password):
        self._cursor.execute("SELECT * from accounts WHERE login=?", login)
        user = self._cursor.fetchall()
        if decrypt_data(user[2]) != password:
            return False # or raise DBManagerError(e)
        else:
            return True


