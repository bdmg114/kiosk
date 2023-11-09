import socket
from _thread import *
import json

def recv_data(client_socket):
    while True:
        data = client_socket.recv(1024)
        print("recive : ", repr(data.decode()))

def init(ip):
    global HOST
    global PORT
    global client_socket

    HOST = ip
    PORT = 9999

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    start_new_thread(recv_data, (client_socket,))

def send_order(order):
    j_order = json.dumps(order)
    client_socket.send(j_order.encode('utf-8'))

def close():
    client_socket.close()

