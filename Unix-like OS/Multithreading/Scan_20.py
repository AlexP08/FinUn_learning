import socket
import tqdm
import threading

n_thread = threading.Thread()

ports = []
N = 49150
for port in tqdm.tqdm(range(1, N + 1)):
    sock = socket.socket()
    try:
        sock.connect(('localhost', port))
        ports.append(port)
    except:
        continue
    finally:
        sock.close()
print("Открытые порты:")
for port in ports:
    print(port)