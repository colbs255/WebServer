import sys

def construct_header(body_size):
    return "HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {}\n".format(body_size)

def create_message(file):
    try:
        body = open_file(file)
    except IOError:
        body = "HTTP/1.1 404 Not Found".encode()
    #have to add another new line before body, must encode when sending
    #body is already encoded
    header = construct_header(len(body)) + "\n"
    return header.encode() + body

#open file in binary for all file types
def open_file(file_name):
    with open(file_name, "rb") as f:
        msg = f.read()
    return msg

def create_text_message(text):
    return "HTTP/1.1 200 OK\nContent-Type: text/plain\nContent-Length: {}\n\n{}".format(len(text), text)

def parse_http(header):
    line = header.split("\r\n")[0]
    line = line.replace("GET /", "", 1)
    line = line.replace(" HTTP/1.1", "", 1)
    return line

