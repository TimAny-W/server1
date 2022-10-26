from socket_server.settings import log_file_path
import datetime


def write_log(data) -> str:
    """Write log to file with path in settings.py
        return original data
    """
    with open(fr'logs.txt', 'a+') as f:
        f.write(f'{data} ||{datetime.datetime.now()}||\n')
    return f'{data} ||{datetime.datetime.now()}||\n'

