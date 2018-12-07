import sys
FILE_NAME = 'index.html'
def construct_header(body_size):
    return "HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {}\n".format(body_size)

def create_message():
    body = open_file(FILE_NAME)
    header = construct_header(len(body))
    return header + "\n" + body

def open_file(file_name):
    f = open(file_name, 'r')
    msg = ''
    with open(file_name) as f:
        msg = f.read()
    return msg