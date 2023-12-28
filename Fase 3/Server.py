import socket
import time
import os

def client():
    
    IP = '192.168.1.124'
    PORT = 8080
    ADDR = (IP, PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    with open(r"C:\Users\User\Desktop\Lockscope\Fase 3\key.pkl", "rb") as f:
        data = f.read()
        client.send("key.pkl".encode())
        time.sleep(2)
        client.send(data)

    client.close()

    try:
        os.remove(r"C:\Users\User\Desktop\Lockscope\Fase 3\key.pkl")
    except FileNotFoundError:
        print("File not found")
    

def receiver():

    IP = '192.168.1.125'
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