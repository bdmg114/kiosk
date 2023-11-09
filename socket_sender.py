import socket
from _thread import *
import json

HOST = '192.168.0.17' ## server에 출력되는 ip를 입력해주세요 ##
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def recv_data(client_socket):
    while True:
        data = client_socket.recv(1024)
        print("recive : ", repr(data.decode()))

start_new_thread(recv_data, (client_socket,))
print('>> Connect Server')

def send_order(order):
    j_order = json.dumps(order)
    client_socket.send(j_order.encode('utf-8'))

def close():
    client_socket.close()

