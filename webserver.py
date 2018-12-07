import socket
from threading import Thread, Lock
import utils
import http.client

SERVER_PORT = 8081
# HOST = socket.gethostbyname(socket.gethostname())
HOST = socket.gethostname()
MAX_CONNECTIONS = 10
s = None

def setup_socket():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, SERVER_PORT))

def listening():
    s.listen(MAX_CONNECTIONS)
    while True:
        connection, addr = s.accept()
        a_thread = Thread(target=handle_client, args=(connection, addr), daemon=True)
        a_thread.start()


def handle_client(connection, addr):
        print('===================Request received=================')
        while True:
                data = connection.recv(2000)
                print(data.decode())
                connection.send(utils.create_message().encode())
        connection.close()

def start():
    print("Connect to {}:{}/index.html".format(HOST, SERVER_PORT))
    setup_socket()
    listening()
start()
