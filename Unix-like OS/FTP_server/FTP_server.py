import socket, os
from pathlib import Path
from Commands import ls, pwd, mkdir, create_file, rmdir, rename, rm, move, cat, hlp


PORT = 9090


def check_command(req):
    comm, *args = req.split()
    try:
        if comm == 'pwd':
            return pwd(*args)
        elif comm == 'ls':
            return ls(*args)
        elif comm == 'mkdir':
            return mkdir(*args)
        elif comm == 'cf':
            return create_file(*args)
        elif comm == 'rmdir':
            return rmdir(*args)
        elif comm == 'rename':
            return rename(*args)
        elif comm == 'rm':
            return rm(*args)
        elif comm == 'move':
            return move(*args)
        elif comm == 'cat':
            return cat(*args)
        elif comm == 'help':
            return hlp(*args)

    except Exception as e:
        return 'Команда не найдена'


home_dir = Path(os.getcwd(), 'your_nome_dir')


def main():

    if not home_dir.is_dir():
        os.mkdir(home_dir)
    os.chdir(home_dir)

    with socket.socket() as sock:
        sock.bind(('', PORT))
        sock.listen()
        print("Слушаю порт:", PORT)
        while True:
            conn, addr = sock.accept()
            with conn:
                req = conn.recv(1024).decode()
                if len(req) > 0:
                    print(req)
                    resp = check_command(req)
                if resp is None:
                    resp = ''
                conn.send(resp.encode())


if __name__ == '__main__':
    main()
