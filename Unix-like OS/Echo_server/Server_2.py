import socket
import time

PORT = 2000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', PORT))

try:
    while True:
        server.listen(1)

        client_socket, address = server.accept()
        print(f'Пользователь {address} присоединился')

        client_socket.send('Вы успешно подключились!'.encode('utf-8'))
        while True:
            try:
                data = client_socket.recv(2048).decode('utf-8')
            except OSError:
                data = None

            time.sleep(1)
            if data:
                print('\nПолучено сообщение:')
                print(data)
            text = input('\nВведите ответ:\n').encode('utf-8')
            client_socket.send(text)
            if text == 'exit'.encode('utf-8'):
                time.sleep(2)
                server.shutdown(socket.SHUT_WR)
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                server.bind(('127.0.0.1', 2000))
                break
except KeyboardInterrupt:
    print('Серевер не подключен')
    server.shutdown(socket.SHUT_WR)
except BrokenPipeError:
    print('Нет подключенных пользователей. Отключаемся!')
    server.shutdown(socket.SHUT_WR)