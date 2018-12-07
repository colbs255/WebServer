import socket
from threading import Thread, Lock
import utils
import http.client
import sys

if len(sys.argv) != 2:
        print('Invalid arguments. Must enter the port number to run on.')
try:
        SERVER_PORT = int(sys.argv[1])
except ValueError:
        print("Port number must be an integer")
        exit(1)
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
        print('===================New Client=================')
        while True:
                data = connection.recv(2000)
                print('=====Request Received=====')
                print(data.decode())
                connection.send(utils.create_message().encode())
        connection.close()

def start():
    print("Connect to {}:{}/index.html".format(HOST, SERVER_PORT))
    setup_socket()
    listening()
start()
