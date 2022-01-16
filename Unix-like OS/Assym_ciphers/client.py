import socket
import pickle
from random import randint


def crypt(a1, key):
    a2 = [chr(ord(a1[i]) ^ key) for i in range(len(a1))]
    return ''.join(a2)


def send(sock, massage1, K):
    massage1 = crypt(massage1, K)
    print("Зашифрованно:  ", massage1)  # Проверка шифра
    sock.send(pickle.dumps(massage1))


def receive(sock, K):
    massage2 = pickle.loads(sock.recv(1024))
    massage2 = crypt(massage2, K)
    return massage2


HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

p, g, a = [randint(0, 250) for i in range(3)]
A = g ** a % p
sock.send(pickle.dumps((p, g, A)))
B = pickle.loads(sock.recv(1024))
K = B ** a % p
print('Enter your message')
msg = input()
while msg != 'exit':
    send(sock, msg, K)
    msg = input()
sock.close()
