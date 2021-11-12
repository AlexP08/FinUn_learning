import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = input('Введите номер порта (или пробел для того чтобы выбрать порт по умолчанию - 2000)\n')
if port == " ":
    port = 2000
else: port = int(port)
name = input('Введите имя хоста (или пробел для того чтобы выбрать хост по умолчанию - localhost)\n')
if name == " ":
    name = "localhost"

try:
    client.connect((name, port))
except (ConnectionRefusedError, socket.gaierror):
    print("Соединение с портом выбраным вами недоступно\nПопробовать порт по умолчанию (порт 2000)? Y\\N")
    if input() == "Y" or "y":
        client.connect(('127.0.0.1', 2000))
    else:
        print('Попытаемся еще раз!')
        exit()
print(client.recv(2048).decode('utf-8'))
try:
    while True:
        client.send(input('Введите ваше сообщение:\n').encode('utf-8'))
        data = client.recv(2048).decode('utf-8')
        time.sleep(1)

        if data.lower() == 'exit':
            print('Все пропало!')
            exit()

        if data:
            print(data)
except KeyboardInterrupt:
    client.shutdown(socket.SHUT_WR)
