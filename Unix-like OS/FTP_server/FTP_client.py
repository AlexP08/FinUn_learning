import socket
PORT = 9090
HOST = 'localhost'

def main():
    print(f"Подключился к {HOST} {PORT}")
    print('help - список команд, exit - выход')
    while True:
        req = input('ftp@youcomm$')
        if req == 'exit':
            break
        with socket.socket() as sock:
            sock.connect((HOST, PORT))

            sock.send(req.encode())
            response = sock.recv(1024).decode()
            if response:
                print(response)


if __name__ == '__main__':
    main()