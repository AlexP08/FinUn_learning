import socket

IP = "localhost"
PORT = 8080
ADDR = (IP, PORT)
DIS_MESSAGE = "EXIT"


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"Клиент подключился, адрес: {IP}:{PORT}")

    while True:
        message = input("> ")
        client.send(message.encode("utf8"))
        if message == DIS_MESSAGE:
            client.send(f"Пользователь:{ADDR} отключен".encode("utf8"))
            break
        else:
            message = client.recv(2000).decode("utf8")
            print(f"[SERVER] {message}")


if __name__ == "__main__":
    main()