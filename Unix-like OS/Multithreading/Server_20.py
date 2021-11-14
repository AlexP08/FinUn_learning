import socket
import threading

IP = "localhost"
PORT = 8080
ADDR = (IP, PORT)
DIS_MESSAGE = "EXIT"


def handle_client(conn, addr):
    print(f"Был подключен: {addr}.")

    while True:
        message = conn.recv(8080).decode("utf-8")
        if message == DIS_MESSAGE:
            break

        print(f"[{addr}] {message}")
        conn.send(message.encode("utf8"))
    conn.close()


def main():
    print("Сервер работает")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(ADDR)
    server.listen()
    print(f"Слушаю!")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Всего подключений: {threading.activeCount() - 1}")


if __name__ == "__main__":
    main()